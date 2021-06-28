import sys
sys.stdin = open("in.txt", "r")

def find(x):
    if parent[x] == x:
        return parent[x]
    return find(parent[x])

def union(x,y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]

test_Case = int(input())

for _ in range(test_Case):
    parent = dict()
    number = dict()

    n = int(input())

    for i in range(n):
        x, y = sys.stdin.readline().split()

        if x not in parent:
            parent[x] = x
            number[x] = 1

        if y not in parent:
            parent[y] = y
            number[y] = 1

        union(x,y)
        print(number[find(x)])