import curses
from file_open_dialog import file_open_dialog
from menu import menu

if __name__ == "__main__":
    mnu = menu(['one', 'two', 'three'])
    print (curses.wrapper (mnu.show))
    fod = file_open_dialog ()
    print (curses.wrapper (fod.show))

