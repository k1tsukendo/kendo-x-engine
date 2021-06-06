from sdl2 import *
from sdl2 import ext
import sys
import ctypes


class KXE_Window(object):
    def __init__(self,
                 size: tuple[int, int] = (640, 480),
                 title: str = 'kxe-window'):
        self.width, self.height = size
        self.title = title
        self.window = ext.Window(title, size)
        self.surface = self.window.get_surface()

    def show(self):
        self.window.show()
        if self.window is None:
            raise TypeError('%s does not exists.')

    def fill(self):
        ext.fill(self.surface, ext.Color(40, 40, 40))
        self.window.refresh()

    def close_event_processor(self):
        event = SDL_Event()
        while True:
            ret = SDL_PollEvent(ctypes.byref(event), 1)
            if ret == 1:
                if event.type == SDL_QUIT:
                    return False
            self.window.refresh()
            timer.SDL_Delay(10)
        ext.quit()
