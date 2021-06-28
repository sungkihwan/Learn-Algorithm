import sys

sys.stdin = open("in.txt", "r")

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

N = int(input())
M = int(input())
parent = dict()

for i in range(N):
    x = sys.stdin.readline()
    


