def divide(num):
    try:
        print(100/num)
    except ZeroDivisionError:
        print("divided by zero.")
    except (ValueError,TypeError):
        print("please enter a number.")
    
print("enter a number")
num=input()
divide(num)

#finally
def fin_divide(num):
    try:
        print("hello")
        print(100/num)
    except ZeroDivisionError:
        print("Divide by zero")
    except (ValueError,TypeError):
        print("You should print a number")
    finally:
        print("the code will run")

fin_divide('a')