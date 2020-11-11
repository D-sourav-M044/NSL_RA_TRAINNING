class Monster :
    identity = 'negative'
    def __init__(self,color,head):
        self.color = color
        self.head = head
    def attack(self):
        print("it's working")
#creation

mournsake   =Monster("red",10)

print("moursake has "+ str(mournsake.head)+" head and it's color is"+ str(mournsake.color))
mournsake.attack()
print(Monster.identity)

class new_class(Monster):
    def check(self):
        print("checked ok")

dinga = new_class("yellow",2)
dinga.check()