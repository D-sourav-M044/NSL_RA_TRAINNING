def hello():
    print("hello world")

hello()

def make_sum( x, y):
    z=x+y
    print(z)
make_sum(5,6)

#multiple_parameter

def make_sum(*arg):
    z=0
    for i in arg:
        z=z+i
    print(z);
make_sum(1,2,3)

def print_dict(**arg):
    print(arg)
print_dict(a=1,b=2,c=3)

def print_all(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)


print_all(10, 20, 30, 50, b=5, c=10)