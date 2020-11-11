class my_nu():
    def __init__(self,num):
        self.num = num
    def __add__(self,other):
        return (self.num + other.num)
    def __mul__(self,other):
        return self.num + other.num
        
a=my_nu(3)
b=my_nu(2)
c=a+b
d=a*b
print(c)
print(d) 

class MyInt():
    def __init__(self, value):
        self.__value = value

    def __int__(self):
        return self.__value


    def __iadd__(self, other):
        return self.__value + int(other) * int(other)


a = MyInt(2)

a += MyInt(3)

print(a)