def my_dec(func):
    def decorate():
        print("+++++++++++++")
        func()
        print("+++++++++++++")
    return decorate

def print_row():
    print("hello")

output=my_dec(print_row)
output()
@my_dec
def prin_text():
    print("hello world")
prin_text()