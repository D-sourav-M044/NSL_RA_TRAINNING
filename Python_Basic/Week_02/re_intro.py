import re

pattern = r"sourav"
password = input("Enter the password : ")
match = re.match(pattern,password)
if match:
    print("password matched")
else:
    print("try again")

#methods
pattern = r"teacher"
rslt = re.search(pattern,"he is a teacher and his son is also a teacher.")
rslt1 = re.findall(pattern,"he is a teacher and his son is also a teacher")
if rslt:
    print("teacher found")
    print(rslt.group())
    print(rslt1)
    print(rslt.start())
    print(rslt.end())
    print(rslt.span())
else:
    print("pattern doesn't matched")
