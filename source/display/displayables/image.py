from sdl2 import *
from sdl2 import ext
import sys, ctypes


class Image(object):
    def __init__(self, path):
        self.path = path

    def __del__(self):
        pass

    def show(self):
        pass
