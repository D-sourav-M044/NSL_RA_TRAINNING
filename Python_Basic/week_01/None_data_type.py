def test_function():
    print("testing")
data = test_function()
print(data)

#testing none 

def another_test(x= None):
    if x:
        print(x*x)
    else:
        print("this is none type")

print(another_test(0))
print(another_test(5))
print(another_test())