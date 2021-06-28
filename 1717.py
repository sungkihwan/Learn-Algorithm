import sys
sys.stdin = open("in.txt", "r")
sys.setrecursionlimit(100000)

def find(x):
    if parent[x] == x:
        return parent[x]
    parent[x] = find(parent[x])
    return parent[x]

def union(x,y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

N, M = map(int,sys.stdin.readline().split())
parent = dict()

for i in range(N+1):
    parent[i] = i

for i in range(M):
    o, a, b = map(int,sys.stdin.readline().split())

    if o == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")

