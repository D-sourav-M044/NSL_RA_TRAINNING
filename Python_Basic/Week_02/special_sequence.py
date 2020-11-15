import re
pattern = r"(.+) \1"

if  re.match(pattern,"world world"):
    print("match -01")
elif re.match(pattern,"worldworld"):
    print("match-02")

pattern = r"(\D+\d)"

match = re.match(pattern, "Hi 999h")

if match:
    print("Match 1")
