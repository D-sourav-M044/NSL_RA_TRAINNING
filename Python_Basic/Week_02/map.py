def is_even(x):
    return x % 2 
num = [1,2,3,4,5]
result = map(is_even,num)
print(list(result))

#filter

def fil(x):
    return x%2 == 0
data = filter(fil,num)
print(list(data))

