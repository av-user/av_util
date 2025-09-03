import curses

from pathlib import Path
import sys

current_dir = Path.cwd()
print (current_dir)
# sys.path.append(str(Path.cwd()))
from av_util import fod

if __name__ == "__main__":
    dlg = fod ()
    print (curses.wrapper (dlg.show))
