import curses

from av_util import console

class key_def:
    TAB = ord ('\t')
    ESC = 27
    QUIT = ord('q')

def foo (stdscr):
    con = console (stdscr, 22, 80, 5, 80, 'debug console')
    def draw_tree():
        _, w = stdscr.getmaxyx()
        title = "test console"
        stdscr.attron(curses.color_pair(2))
        stdscr.addstr(1, w//2 - len(title)//2, title)
        stdscr.attroff(curses.color_pair(2))
        x = 2
        stdscr.refresh()
        # workaround()
        con.workaround()

    while True:
        draw_tree()
        key = stdscr.getch()
        match key:
            case key_def.ESC | key_def.QUIT:
                break
            case _:
                con.append (f'key {key} pressed')
                pass

if __name__ == "__main__":
    print (curses.wrapper (foo))
