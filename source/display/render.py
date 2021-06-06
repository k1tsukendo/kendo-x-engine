from sdl2 import *
from sdl2 import ext

from .window import KXE_Window
from .displayables.image import Image


class Renderer(object):
    def __init__(self, window: KXE_Window):
        if window != KXE_Window:
            quit(print('You need to use KXE_Window object!'))

        self.window = window
        self.texture_renderer = ext.Renderer(window)
        self.sprite_renderer = ext.TextureSpriteRenderSystem(self.texture_renderer)
        self.sprite_factory = ext.SpriteFactory(ext.TEXTURE, render=self.texture_renderer)

        self.sprite_factory.create_sprite_render_system()

    def render_image(self, target: Image):
        img = self.sprite_factory.from_image(target.path)
