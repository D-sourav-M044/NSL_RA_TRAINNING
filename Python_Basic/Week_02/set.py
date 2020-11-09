num =[1,2,3]
data = set(["banana","mango","apple"])
data1= ["banana","mango","apple"]
print(3 in num)
print("mango" in data)
print(data)
print(data1)
data1[2]="jam"

list_data =[1,2,2,3]
set_data=set(list_data)
print(set_data)

data1={1,2,3,4,5}
data2={5,6,7,8,9,10}
print(data1 | data2)
print(data1 & data2)
print(data1-data2)
print(data1^data2)