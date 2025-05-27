
import json as js

class SaveSetting:
    def __init__(self, width: int, height: int, fps: int, fs: bool, bgm_vol: float, sfx_vol: float):
        self.width = width
        self.height = height
        self.fps = fps
        self.fs = fs
        self.bgm_vol = bgm_vol
        self.sfx_vol = sfx_vol 
    def save(self):
        self.saveSetting = { "width" : self.width, "height" : self.height, "fps" : self.fps, "fs" : self.fs, "bgm_vol" : self.bgm_vol, "sfx_vol" : self.sfx_vol }
        with open("./Option/settings.json", "w") as f:
            js.dump(self.saveSetting, f)
        