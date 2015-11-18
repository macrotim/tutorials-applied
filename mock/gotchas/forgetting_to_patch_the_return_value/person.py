class Person(object):
    def __init__(self):
        self.pet = Pet()

class Pet(object):
    def noise(self):
        return "Woof"
