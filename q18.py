# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.

class Product:
    def __init__(self,price):
       self._price=price
    @property
    def get_price(self):
        print("getter calling...")
        print(self._price)
        
    @get_price.setter
    def get_price(self, value):
        print("setter calling...")
        if 0<value:
            self._price=value
        else:
            print("Invalid Price")
            
    @get_price.deleter
    def get_price(self):
        print("Deleter calling...")
        del self._price
        
p1=Product(500)
p1.get_price  #500
p1.get_price=1000 #call setter
p1.get_price #100
del p1.get_price  #call deleter
p1.get_price #raise error coz price not found
 