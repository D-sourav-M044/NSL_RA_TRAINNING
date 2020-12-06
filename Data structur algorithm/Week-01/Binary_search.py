
def search(data,num):
    begin = 0
    end = len(data)-1
    index = None
    while begin<=end:
        mid = int((begin+end)/2)
        if num == data[mid]:
            index = mid
            break
        elif num>data[mid]:
            begin = mid+1
        elif num<data[mid]:
            end = mid-1
    return index



info = [10,60,70,80,40,100,120]
info = sorted(info)
print(info)

while True:
    x = int(input())
    y = search(info,x)
    print(y)