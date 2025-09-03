from collections import deque
import curses

class console_window(object):
    def __init__(self, stdscr, h: int, w: int, y: int, x: int, title: str = 'console'):
        self._stdscr = stdscr
        self._queue = deque (maxlen=h - 2)
        self._win = curses.newwin (h, w, y, x)
        self._title = title
    def workaround (self):
        self._win.box()
        self._win.addstr(0, 2, f' {self._title} ')
        self._win.refresh()
    def draw_console (self):
        for i, s in enumerate(self._queue):
            self._win.move(i+1, 2)
            self._win.clrtoeol()
            self._win.addstr(i+1, 2, s)
        self._win.box()
        self._win.addstr(0, 2, f' {self._title} ')
        self._win.refresh()

    def append(self, line: str) ->None:
        self._queue.append (line)
        self.draw_console()




