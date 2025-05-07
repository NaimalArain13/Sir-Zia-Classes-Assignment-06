# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.

class Teacher():
    def __init__(self, subject):
        self.subject=subject
class Person(Teacher):
    def __init__(self, name, subject):
        super().__init__(subject)
        # print(subject) 
        self.name=name
    
prsn=Person("Naimal", "Maths")
print(prsn.name)
print(prsn.subject)