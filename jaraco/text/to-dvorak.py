import sys

from . import layouts

if __name__ == '__main__':  # pragma: nocover
    layouts._translate_stream(sys.stdin, layouts.to_dvorak)
