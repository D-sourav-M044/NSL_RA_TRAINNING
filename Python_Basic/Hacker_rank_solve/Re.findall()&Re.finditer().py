import re
from typing import Pattern
s = '[qwrtypsdfghjklzxcvbnm]'
#a = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I)
#print('\n'.join(a or ['-1']))

cons = '[abcdfghjklmnpqrstvwxyz]'
Pattern = re.findall('(?<=' + cons +')([aeiou]{2,})' + s, input(), re.I)
print("\n".join(Pattern or ['-1']))