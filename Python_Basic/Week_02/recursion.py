def fact(x):
    if x==1:
        return 1
    else:
        return x*fact(x-1)
print(fact(5))

def is_even(x):
    if x==0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

print(is_even(14))
print(is_odd(13))