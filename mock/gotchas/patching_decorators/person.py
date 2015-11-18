from decorators import noise_logger

class Person(object):
    def __init__(self):
        self.pet = Pet()

class Pet(object):
    @noise_logger
    def noise(self):
        return "Woof"
