import curses

from pathlib import Path
import sys

current_dir = Path.cwd()
print (current_dir)
# sys.path.append(str(Path.cwd()))
from av_util import input_box

if __name__ == "__main__":
    inbox = input_box (10, 5, 20, 'text')
    print (curses.wrapper (inbox.show))
