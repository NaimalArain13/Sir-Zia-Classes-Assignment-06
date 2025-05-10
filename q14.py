# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Department:
    def __init__(self, name):
        self.name=name

class Employee:
    def __init__(self,name) :
        self.name=name
        self.department=[]
    def add_department(self, department):
        self.department.append(department)
        
fin=Department("Finance")
acd=Department("Academic")
employee1=Employee("Bob")
employee1.add_department(fin)
employee1.add_department(acd)

print(employee1.name)
for departement in employee1.department:
    print(departement.name)