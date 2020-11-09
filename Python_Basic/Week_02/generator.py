def my_it():
    i=5
    while i>=5:
        yield i
        i -=1
for i in my_it():
    print(i)