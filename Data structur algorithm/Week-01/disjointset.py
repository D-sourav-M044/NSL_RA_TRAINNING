elements = 5
par=[None]*(elements+1)

for i in range(1,elements+1):
    par[i] =i

def find(a):
    if par[a]==a:
        return a
    else:
        par[a]=find(par[a])
    return par[a]

def union(a,b):
    u = find(a)
    v = find(b)
    if u==v:
        print("already in a same set")
    else:
        par[v] = u

