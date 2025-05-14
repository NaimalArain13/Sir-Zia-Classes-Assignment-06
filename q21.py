# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. Implement __iter__() and __next__() to make the object iterable in a for-loop, counting down to 0.

class Countdown:
    def __init__(self, count:int):
        self.count=count
    def __iter__(self):
        return MyIterator(self.count)

class MyIterator:
    def __init__(self, count):
        self.count=count
    def __next__(self):
        if self.count<0:
            raise StopIteration
        value=self.count
        self.count-=1
        return value

for item in Countdown(4):
    print(item)
        