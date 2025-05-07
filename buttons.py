
import random as rand

class Buttons:
    def __init__(self, Buttons: list[str]):
        self.Buttons_list = Buttons
    def getRand(self):
        self.Rand = rand.randint(0, len(self.Buttons_list)-1)
        return self.Rand
    def getSR(self, type: int):
        self.type = type
       #self.Button = None
        if self.type == 0:
            self.Button = self.Buttons_list[type]
            return tuple((self.Button.convert_alpha(), self.Button.get_rect()))
        if self.type == 1:
            self.Button = self.Buttons_list[type]
            return tuple((self.Button.convert_alpha(), self.Button.get_rect()))
        if self.type == 2:
            self.Button = self.Buttons_list[type]
            return tuple((self.Button.convert_alpha(), self.Button.get_rect()))
    
        