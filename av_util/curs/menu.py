import curses

class key_def:
    ESC = 27
    QUIT = ord('q')

class menu(object):
    def __init__(self, items: list):
        self._items = items

    def show(self, stdscr):
        # Setup
        curses.curs_set(0)  # Hide cursor
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)

        current_row = 0

        def draw_menu():
            stdscr.clear()
            h, w = stdscr.getmaxyx()
            title = "Use ↑ ↓ to navigate, Enter to select, Esc or 'q' to cancel"
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(1, w//2 - len(title)//2, title)
            stdscr.attroff(curses.color_pair(2))

            for idx, item in enumerate(self._items):
                x = w//2 - len(item)//2
                y = h//2 - len(self._items)//2 + idx
                if idx == current_row:
                    stdscr.attron(curses.color_pair(1))
                    stdscr.addstr(y, x, item)
                    stdscr.attroff(curses.color_pair(1))
                else:
                    stdscr.addstr(y, x, item)
            stdscr.refresh()

        while True:
            draw_menu()
            key = stdscr.getch()
            match key:
                case key_def.ESC | key_def.QUIT:
                    break
                case curses.KEY_UP:
                    current_row = len(self._items)-1 if current_row == 0 else current_row - 1
                case curses.KEY_DOWN:
                    current_row = 0 if current_row == len(self._items) - 1 else current_row + 1
                case  key if key in [curses.KEY_ENTER, ord('\n')]:
                    return self._items [current_row]