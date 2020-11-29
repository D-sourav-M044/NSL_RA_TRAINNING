import re
from typing import Pattern
s = input()
Pattern = r'([A-Z a-z 0-9|])\1'
m = re.search(Pattern,s)
if m:
    print (m.groups()[0])
else:
    print (-1)
