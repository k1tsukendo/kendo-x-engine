import sys
from display.window import KXE_Window
from kxmath import vector


def main():
    win = KXE_Window()
    win.show()
    win.fill()
    win.close_event_processor()


if __name__ == '__main__':
    sys.exit(main())
