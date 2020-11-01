my_marks= {"bangla" : 80,"english":78,"math":[90,87,88]}
print(my_marks["math"])
print(my_marks.keys())
test = { True : 'ok'}
print(test[True])

my_dic={1:"one",2:"two"}
print(my_dic)
my_dic[3]="three"
print(my_dic)

#get_method
print(my_dic.get(5,"that's not in dictionary"))

rank = [1,2,3]
fruit = ['magno','apple','banana']
dic = {}
dic = {rank[i] : fruit[i] for i in range(len(fruit))}
print(dic)

for i in rank:
    for j in fruit:
        print(i)
        print(j)