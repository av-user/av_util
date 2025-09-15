import curses

class input_box(object):
    def __init__(self, x, y, maxlen, title: str=''):
        self._x = x
        self._y = y
        self._maxlen = maxlen
        self._title = title

    def show(self, stdscr):
        # Setup
        curses.curs_set(1)      # Show the cursor
        curses.echo()           # Echo user input
        curses.start_color()
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_CYAN)
        curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        # Clear and refresh the screen
        stdscr.clear()
        stdscr.refresh()
        
        # Input box dimensions and position
        box_height, box_width = 3, self._maxlen + 2
#        box_y, box_x = 5, 10
        
        # Create input window and draw box
        input_win = curses.newwin(box_height, box_width, self._y, self._x)
        input_win.box()
        input_win.refresh()
        # Create a subwindow inside the box for input
        input_pad = input_win.derwin(1, box_width - 2, 1, 1)
        input_pad.refresh()
        if self._title != '':
            h, w = stdscr.getmaxyx()
            stdscr.attron(curses.color_pair(2))
            stdscr.addstr(1, w//2 - len(self._title)//2, self._title)
            stdscr.attroff(curses.color_pair(2))
            stdscr.refresh()
        # Get user input from the subwindow
        user_input = input_pad.getstr(self._maxlen).decode("utf-8")
        # Redraw the box after input
        input_win.box()
        input_win.refresh()
        return user_input
