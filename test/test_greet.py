from pathlib import Path
import sys

current_dir = Path.cwd()
sys.path.append(str(Path.cwd()))
from av_util import greet

def test_greet():
    print (greet("Alice"))

if __name__ == '__main__':
    test_greet()
