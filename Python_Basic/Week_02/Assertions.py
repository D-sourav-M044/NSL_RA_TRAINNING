print(1)
assert 1==1

def kel_to_far(temp):
    assert (temp >=0)
    return ((temp -273)*1.8)+32

print(kel_to_far(34))
print(kel_to_far(-3))