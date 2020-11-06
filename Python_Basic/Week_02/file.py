file = open("data.txt","r")
#content =file.read()
line = file.readlines()
content = file.read()
#print(content)
print(line)
file.close()
print("this is closed now")
file =open("data.txt","r")
for line in file:
    print(line)
file.close()

#writing
file = open("data.txt",'w')
dt_write=file.write("here is my data")
if dt_write:
    print("yes ,{0} bytes has been written".format(dt_write))
file.close()
file= open("data.txt","r")
content = file.read()
print(content)
file.close()