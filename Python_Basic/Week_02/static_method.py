class pizza:
    def __init__(self,toppings):
        self.toppings = toppings
    @staticmethod
    def valid_topping(topping):
        if topping == "pinaapple":
            raise ValueError("NO pinapple")
        else:
            return True
fruits =["mango","banana","pinaapple"]
if all(pizza.valid_topping(i) for i in fruits):
    #pizza = pizza(fruits)
    print(pizza(fruits))