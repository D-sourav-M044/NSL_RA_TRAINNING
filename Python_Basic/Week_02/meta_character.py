import re

pattern = r'.'
data = input("enter here : ")
if re.match(pattern,data):
    print("matched")
else:
    print("no match")

pattern = r"(?P<first>abc)(?:def)(ghi)"
#pattern = r"(?P<first>abc)(?:def)(ghi)"
match = re.match(pattern,"defghi")
if match :
    print("ekhane")
    print(match.group("first"))
    print(match.group())