
import json as js

class SaveSetting:
    def __init__(self, width: int, height: int, fps: int, fs: bool):
        self.width = width
        self.height = height
        self.fps = fps
        self.fs = fs

    def save(self):
        self.saveSetting = { "width" : self.width, "height" : self.height, "fps" : self.fps, "fs" : self.fs }
        with open("./SaveData/setting.json", "w") as f:
            js.dump(self.saveSetting, f)
        