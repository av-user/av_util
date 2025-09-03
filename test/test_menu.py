import curses

from pathlib import Path
import sys

current_dir = Path.cwd()
print (current_dir)
# sys.path.append(str(Path.cwd()))
from av_util import menu

if __name__ == "__main__":
    m = menu (['one', 'two', 'three'])
    print (curses.wrapper (m.show))
