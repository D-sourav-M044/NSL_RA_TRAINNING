class queue:
    def __init__(self,content):
        self.list = content
    def push(self,data):
        self.list.insert(0,data)
    def pop(self):
        self.list.pop(-1)
    def _show(self):
        return self.list
my_list=[1,2,3]
a = queue(my_list)
a.push(3)
print(a._show())
a.pop()
print(a._show())

#strongly_private

class safe:
    __safe_data = 10

    def show_data(self):
        print(self.__safe_data)

cl = safe()
cl.show_data()
print(cl._safe__safe_data)
print(cl.__safe_data)