import curses
import os
import fnmatch
from pathlib import Path

from .console_window import console_window as console

class key_def:
    TAB = ord ('\t')
    ESC = 27
    QUIT = ord('q')

class file_open_dialog(object):
    def __init__(self, filetypes: list = [("All files", "*.*")]):
        self._filetypes = filetypes
    def show (self, stdscr)->Path:
        # print(type(console))
        con = console (stdscr, 22, 80, 5, 80, 'debug console')
        def workaround():
            # the system needs this under some circumstances.
            # it must 'clear its throat' this way — otherwise, for unknown reasons,
            # the windows disappear before the first key is pressed.
            # try to bypass it and you will see.
            curses.ungetch(curses.KEY_MIN)
            stdscr.getch()

        # Setup
        curses.curs_set(0)  # Hide cursor
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

        items = []
        count_folders = 0
        count_files = 0

        FIRST_ROW_OFFSET = 3    #the first three lines dedicated to title, an empty line and current path
        current_row = 0
        page_offset = 0
        def prt (s:str)->None:
            stdscr.addstr(20, 5, s)
            stdscr.addstr(21, 5, 'press any key')
            stdscr.getch()
            stdscr.move(21, 5)
            stdscr.clrtoeol()
        def draw_tree(path: Path):
            nonlocal items, count_folders, count_files, con
            folders = []
            files = []
            count_folders = 1   #because of parent folder string '..' or ''
            count_files = 0
            # Loop through all items in the directory
            for item in os.listdir(path):
                full_path = os.path.join(path, item)
                if os.path.isdir(full_path):
                    folders.append(item)
                    count_folders += 1
                elif os.path.isfile(full_path):
                    filename = os.path.basename(full_path)
                    patterns = [pattern for _, pattern in self._filetypes]
                    if any(fnmatch.fnmatch(filename, pattern) for pattern in patterns):
                        files.append(item)
                        count_files += 1
            if path.resolve().anchor == str(path.resolve()):
                items = [('', True),]
            else:
                items = [('..', True),]

            for item in folders:
                items.append ((item, True))
            for item in files:
                items.append ((item, False))
            stdscr.clear()
            h, w = stdscr.getmaxyx()

            for i in range (h):
                stdscr.addstr(i, 74, f'{i}')

            title = "Find a file using ↑ ↓ ⇞ ⇟ to navigate, Enter to select, Esc or 'q' to cancel"
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(1, w//2 - len(title)//2, title)
            stdscr.attroff(curses.color_pair(2))
            x = 2
            stdscr.addstr(FIRST_ROW_OFFSET - 1, x, str(path))
            y = FIRST_ROW_OFFSET
            try:
                for idx, item in enumerate (items[page_offset:]):
                    if idx == current_row - page_offset:
                        stdscr.attron(curses.color_pair(1))
                    if item[1]: #folder, not file
                        connector = '└──' if idx == count_folders - page_offset - 1 else '├──'
                        stdscr.addstr(y, x, f'{connector} [DIR] {item[0]}')
                    else: #file
                        x = 6
                        connector = '└──' if idx == len(items) - page_offset - 1 else '├──'
                        stdscr.addstr(y, x, f'{connector} {item[0]}')
                    if idx == current_row - page_offset:
                        stdscr.attroff(curses.color_pair(1))
                    y += 1
            except curses.error:
                pass
            stdscr.refresh()
            workaround()
            con.workaround()

        current_folder = Path.cwd()
        while True:
            draw_tree(current_folder)
            hight, width = stdscr.getmaxyx()
            page_size = hight - (FIRST_ROW_OFFSET)
            items_listed = min (page_size, max (0, len(items) - page_offset))
            key = stdscr.getch()
            match key:
                case key_def.ESC | key_def.QUIT:
                    break
                case curses.KEY_UP:
                    if page_offset == current_row:
                        #do to the last page row
                        current_row = max (0, items_listed - 1) + page_offset
                    else:
                        current_row = current_row - 1 if current_row >= 0 else len(items) - 1
                case curses.KEY_DOWN:
                    current_row = current_row + 1 if current_row < len(items) - 1 and current_row - page_offset < page_size else page_offset
                case curses.KEY_PPAGE:
                    if page_offset:
                        step_size = 2
                        page_offset = max (0, page_offset - page_size)
                        current_row = page_offset
                case curses.KEY_NPAGE:
                    items_tail_outside = max (0, len(items) - page_size - page_offset)
                    if items_tail_outside:
                        page_offset += page_size
                        current_row = page_offset
                case  key if key in [curses.KEY_ENTER, ord('\n')]:
                    if current_row < count_folders:
                        if current_row == 0:
                            current_folder = current_folder.parent
                        else:
                            current_folder = current_folder / items[current_row][0]
                            current_row = 0
                        page_offset = 0
                    else:
                        return current_folder / items[current_row][0]
                    stdscr.clear()
                    workaround()





