# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.

class Bank():
    bank_name="Habib Bank"
    @classmethod
    def change_bank_name(cls, name):
        print(cls.bank_name)
        cls.bank_name=name
        print(cls.bank_name)
    
   
Bank.change_bank_name("Allied Bank") 

   
  