# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.

class Employee():
   
    def __init__(self,name, salary, ssn):
        self.name=name
        self._salary=salary
        self.__ssn=ssn
employee=Employee("Shahid", 500000, 120)
print(employee.name)
print(employee._salary)
print(employee.__ssn)  #AttributeError due to name mangling
# print(employee._Employee__ssn)  #uncomment this line to see the ssn (social security number)