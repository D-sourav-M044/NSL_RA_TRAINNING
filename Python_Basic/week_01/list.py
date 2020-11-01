data = [1,2,3]
print(data + [4,5,6])
print(3 in data)
print([2] in data)

#append
data.append(10);
print(data)

#insert
data.insert(1,'b')
print(data)

#index
print(data.index('b'))
try:
    print(data.index(5))
except :
    print("the searching element is not in list")

#count
print(data.count(2))

#build_in_function
data = [1,2,4]
char =['a','b','c']
print(max(data))
print(min(data))
print(max(char))

#range 
data =list(range(5,50,5))
print(data)

data = [1,2,3,4,5]
print(data[2:4])
print(data[2:-1])
print(data[::-1])
new_data = data[::-1]
print(new_data)

matrix_1d =[]
matrix_2d = [[2,3,4],
            [1,2,3]]
for row in matrix_2d:
    for num in row:
        matrix_1d.append(num)
print(matrix_1d)

#list_comprehensio:

#vowel = ['a','e','i','o','u']
vowel = 'aeiou'
sentence = "i am a kuetian"
new_sentence = ''.join(i for i in sentence if i not in vowel )
print(new_sentence)