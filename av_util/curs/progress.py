import curses
import time

def draw_progress_bar(stdscr, progress, max_width=50, success=True):
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    # Initialize color pairs
    curses.start_color()
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)  # Yellow
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)   # Green
    curses.init_pair(3, curses.COLOR_RED, curses.COLOR_BLACK)     # Red

    # Determine color
    if progress < 1.0:
        color = curses.color_pair(1)
    else:
        color = curses.color_pair(2) if success else curses.color_pair(3)

    bar_width = int(progress * max_width)
    bar = "█" * bar_width
    percent = f"{int(progress * 100)}%"

    # Center the bar
    x = (width - max_width) // 2
    y = height // 2

    stdscr.attron(color)
    stdscr.addstr(y, x, bar)
    stdscr.attroff(color)

    stdscr.addstr(y + 1, x + (max_width // 2) - len(percent) // 2, percent)
    stdscr.refresh()

def main(stdscr):
    curses.curs_set(0)  # Hide cursor
    for i in range(101):
        progress = i / 100
        draw_progress_bar(stdscr, progress, success=False)  # Replace with your condition
        time.sleep(0.05)

    # Show final message
    stdscr.addstr(curses.LINES - 2, 2, "Press any key to exit...")
    stdscr.refresh()
    stdscr.getch()  # Wait for key press

curses.wrapper(main)
