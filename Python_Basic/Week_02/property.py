class pizza:
    def __init__(self,toppings):
        self.toppings = toppings
    @property
    def pineapple_allowed(self):
        return False
    
pizza = pizza(["mango","tomato"])
print(pizza.pineapple_allowed)
#pizza.pineapple_allowed = True 

#using getter & setter

class pizza:
    def __init__(self,toppings):
        self.toppings = toppings
        self._pineapple_allowed = False
    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed
    @pineapple_allowed.setter
    def pineapple_allowed(self,value):
        if value:
            password = input("enter the password")
            if password == "sourav":
                self._pineapple_allowed = value
            else:
                raise ValueError("Get lost")

pizza = pizza(["mango","tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True 
print(pizza.pineapple_allowed)
