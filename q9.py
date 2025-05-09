# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self,length:int, width:int ):
        self.length=length
        self.width=width
    def area(self):
        print(f"Area of Rectange is {self.length*self.width}")
area1=Rectangle(4, 8)
area1.area()