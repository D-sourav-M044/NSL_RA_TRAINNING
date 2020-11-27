import re
pattern = r'(.)*'
s = input()
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        print(i)
        break