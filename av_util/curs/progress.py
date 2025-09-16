import curses

class progress (object):
    
    def __init__(self, max_width: int = 50, title: str=''):
        self._max_width = max_width
        self._title = title
        # Initialize color pairs
        curses.start_color()
        curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Yellow
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)   # Green
        curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)     # Red
        curses.curs_set(0)  # Hide cursor

    def show(self, stdscr, progress: int, success: bool = True):
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        # Determine color
        if progress < 100:
            color = curses.color_pair(1)
        else:
            color = curses.color_pair(2) if success else curses.color_pair(3)

        bar_width = int(progress * self._max_width / 100)
        bar = "█" * bar_width
        percent = f"{progress}%"

        # Center the bar
        x = (width - self._max_width) // 2
        y = height // 2

        stdscr.attron(color)
        stdscr.addstr(y, x, bar)
        stdscr.attroff(color)

        stdscr.addstr(y + 1, x + (self._max_width // 2) - len(percent) // 2, percent)
        stdscr.refresh()
