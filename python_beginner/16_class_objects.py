# Defining a class Human with attributes and methods

class Human:
    def __init__(self, n, o):       # Constructor to initialize name and occupation
        self.name = n
        self.occupation = o

    def do_work(self):              # Method to perform work based on occupation
        if self.occupation == "tennis player":
            print(self.name,"plays tennis")
        elif self.occupation == "actor":
            print(self.name,"shoots a film")

    def speaks(self):   
        print(self.name,"says how are you?")

tom = Human("tom cruise", "actor")
tom.do_work()
tom.speaks()

maria = Human("maria sharapova","tennis player")
maria.do_work()
maria.speaks()