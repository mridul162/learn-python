class Teacher():
    def skills(self):
        print("Teaching")

class YouTuber():
    def skills(self):
        print("Content creator")

class Student(Teacher, YouTuber):
    def skills(self):
        Teacher.skills(self)
        YouTuber.skills(self)
        print("Master Degree")

s= Student()
s.skills()