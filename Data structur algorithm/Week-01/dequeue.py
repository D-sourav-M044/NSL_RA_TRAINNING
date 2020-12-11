from Queue import deque
from typing import Deque


def sliding_rmq(arr,m):
    dq = Deque()
    res = []
    for i,val in enumerate(arr):
        while len(dq) and dq[0][0]>=val:
            dq.popleft()
        dq.append((val,i))
        while len(dq) and dq[-1][1]<i-m:
            dq.pop()
        if i>=m-1:
            print(dq[-1][0])
            res.append(dq[-1][0])
    return res

arr = [10,50,15,12,4]
print(sliding_rmq(arr,3))