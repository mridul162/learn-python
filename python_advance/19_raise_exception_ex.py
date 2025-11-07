class AdultException(Exception):
    def __init__(self, msg):
        self.msg = msg
    def handle(self):
        print("The person is an adult")

# try:
#     raise AdultException('Adult')
# except AdultException as e:
#     e.handle()
#     print(e)

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_minor_age(self):
        if int(self.age) >= 18:
            try:
                raise AdultException("Adult")
            except AdultException as e:
                e.handle()
        else:
            return self.age

    def display(self):
        try:
            print(f"Age: {self.get_minor_age()}")
        except AdultException:
            print("Person is an adult")
        finally:
            print(f"Name: {self.name}")


p = Person("Mridul", 10)
p.display()
q = Person("Asif", 29)
q.display()
# Person("Bhavin", 17).display()
# Person("Dhaval", 23).display()

