import curses

class input(object):
    def __init__(self, x, y, maxlen):
        self._x = x
        self._y = y
        self._maxlen = maxlen

    def show(self, stdscr):
        # Setup
        curses.curs_set(1)      # Show the cursor
        curses.echo()           # Echo user input
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
        # Get user input from the subwindow
        user_input = input_pad.getstr(input_max_len).decode("utf-8")
        # Redraw the box after input
        input_win.box()
        input_win.refresh()
        return user_input



def main(stdscr):
    curses.curs_set(1)      # Show the cursor
    curses.echo()           # Echo user input
    # Clear and refresh the screen
    stdscr.clear()
    stdscr.refresh()
    input_max_len = 20
    # Input box dimensions and position
    box_height, box_width = 3, input_max_len+2
    box_y, box_x = 5, 10
    
    # Create input window and draw box
    input_win = curses.newwin(box_height, box_width, box_y, box_x)
    input_win.box()
    input_win.refresh()
    # Create a subwindow inside the box for input
    input_pad = input_win.derwin(1, box_width - 2, 1, 1)
    input_pad.refresh()
    # Get user input from the subwindow
    user_input = input_pad.getstr(input_max_len).decode("utf-8")
    # Redraw the box after input
    input_win.box()
    input_win.refresh()
    # Display the result below the box
    stdscr.addstr(box_y + 4, box_x, f"You typed: {user_input}")
    stdscr.refresh()
    stdscr.getch()  # Wait for key press before exiting
    
curses.wrapper(main)
