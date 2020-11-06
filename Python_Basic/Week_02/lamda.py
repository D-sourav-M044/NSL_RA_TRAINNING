def my_func(func,arg):
    return func(arg)

print(my_func(lambda x:2*x,5))
a = lambda x:2*x
print(my_func(a,5))
print((lambda x,y:x+2*y)(2,3))