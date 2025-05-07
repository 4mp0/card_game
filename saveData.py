
import json as js

class SaveData:
    def __init__(self, name: str, level: int):
        self.name = name
        self.level = level

    def save(self):
        self.saveData = { "Player" : self.name, "Stage" : self.stage }
        with open("./SaveData/data.json", "w") as f:
            js.dump(self.saveData, f)
        