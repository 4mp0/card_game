
import json

class Setting:
    def __init__(self, width: int, height: int, fps: int, fullscreen: bool):
        self.width = width
        self.height = height
        self.fps = fps
        self.fullscreen = fullscreen
    def get_width(self):
        return self.width
    def get_height(self):
        return self.height
    def get_fps(self):
        return self.fps
    def get_fullscreen(self):
        return self.fullscreen