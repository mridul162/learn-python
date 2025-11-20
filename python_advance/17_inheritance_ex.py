# Inheritance Example
class Animal:
    def __init__(self, habitat):  # Constructor with habitat parameter
        self.habitat = habitat    # Initialize habitat attribute

    def print_habitat(self):      # Method to print habitat
        print(self.habitat)

    def sound(self):
        print("Some Animal Sound")

class Dog(Animal):                # Dog class inherits from Animal
    def __init__(self):
        super().__init__("Kennel")

    def sound(self):              # Overriding the sound method
        print("Woof woof!")

x = Dog()
x.print_habitat()
x.sound()

