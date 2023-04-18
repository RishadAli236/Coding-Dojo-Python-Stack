from modules import pet

class Cat(pet.Pet):
    def __init__(self, name, type, tricks, breed, sound):
        super().__init__(self, name, type, tricks)
        self.breed = breed
        self.sound = sound
    
    def sleep(self):
        super().sleep()

    def eat(self):
        super().eat()

    def play(self):
        super().play()

    def noise(self):
        super().noise()