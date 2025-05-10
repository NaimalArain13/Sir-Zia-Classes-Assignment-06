# 13. Composition
# Assignment:
# Create a class Engine and a class Car. Use composition by passing an Engine object to the Car class during initialization. Access a method of the Engine class via the Car class.

class Engine:
    def start(self):
        return "Engine is starting"
        
class Car:
    def __init__(self):
        self.engine=Engine()
    def start(self):
        print(f"Car Starting: {self.engine.start()}")
car1=Car()
car1.start()