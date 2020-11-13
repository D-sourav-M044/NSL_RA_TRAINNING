t=int(input())
for i in range(t):
    a,b=  map(str,input().split())
    
    try:
        print(int((int(a)/int(b))))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError:
        try:
            a=int(a)
            print("Error Code: invalid literal for int() with base 10: '{0}'".format(b))
        except:
             print("Error Code: invalid literal for int() with base 10: '{0}'".format(a))