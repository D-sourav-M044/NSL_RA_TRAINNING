#string_Formating

msg ="my name is : {x} ".format(x='sourav')
data = "here is my name : {x} and i want {y} money from you.".format(x='sourav',y=250)
print(msg)
print(data)

#string_join:

print("+".join(['apple','mango']))
print(msg)
print(msg.replace("sourav","dipto"))

#startswith/endswith
print("this is ok".startswith("this"))
print("This is ok".startswith("this"))
print("This is a statement".endswith("statement"))

#Upper/Lower
print("hello buddy".upper())
print("HEy dude".lower())

#split
txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(", ")

print(x)