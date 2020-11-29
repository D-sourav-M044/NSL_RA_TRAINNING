if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    list =[]
    for i in arr:
        list.append(i)
    
    a = max(list)
    while max(list) ==a:
        list.remove(max(list))
    print(max(list))
