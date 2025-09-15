import curses

class message_box(object):
    def __init__(self, message: str):
        self._message = message
    def show(self, stdscr):
        # Setup
        curses.curs_set(0)      # Hide the cursor
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        # Clear and refresh the screen
        stdscr.clear()
        stdscr.refresh()
        h, w = stdscr.getmaxyx()
        stdscr.attron(curses.color_pair(2))
        title = 'Press any key to close'
        stdscr.addstr(1, w//2 - len(title)//2, title)
        stdscr.attroff(curses.color_pair(2))
        stdscr.attron(curses.color_pair(1))
        stdscr.addstr(10, w//2 - len(self._message)//2, self._message)
        stdscr.attroff(curses.color_pair(1))
        stdscr.refresh()
        stdscr.getch()  # Wait for key press
