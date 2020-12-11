q = []
head = -1
tail = -1
starpoint = 2
capacity = 5
q = [None for i in range(0,capacity)]
def enque(value):
    global head
    global tail
    global capacity
    global starpoint
    if (tail+1)%capacity == head:
        print(" the queue is full")
        return
    if head == -1:
        head = starpoint
        tail = head
        q[tail] = value
    else:
        tail = (tail+1)%capacity
        q[tail] = value
def deque():
    global head
    global tail
    global capacity
    global starpoint
    if head == -1 :
        print("the queue is already empty")
        return
    q[head] = None
    if head == tail:
        head =-1
        tail =-1
    else:
        head = (head+1)%capacity

enque(2)
enque(3)
enque(4)
enque(5)
enque(6)
enque(7)
print(q)
deque()
print(q)

from typing import Deque


