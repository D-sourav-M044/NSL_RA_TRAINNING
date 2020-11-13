def merge_the_tools(string, k):
    size = len(string)
    sub_size=size/k
    ind=0
    if k==1:
        for i in range(len(string)):
            print(string[i])
    else:
        for i in range(k):
            sub_string = string[ind:ind+k]
            ans = ""
            for j in range(len(sub_string)):
                if sub_string[j] not in ans:
                    ans+=sub_string[j]
            print(ans)
            ind+=k
