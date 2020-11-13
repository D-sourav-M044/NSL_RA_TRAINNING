class test:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height
    @classmethod
    def new_test(cls,length,data):
        return cls(length,data)

a = test.new_test(3,4)
print(a.area())
