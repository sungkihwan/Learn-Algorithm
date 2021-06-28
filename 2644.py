import sys
from collections import deque
sys.stdin = open("in.txt", "r")

def bfs(start):
    q = deque()
    q.appendleft(start)
    while q:
        n = q.pop()
        if n not in visited:
            visited.append(n)
            q.extendleft(graph[n])
            rank[n] = 1
    return print(visited, rank)


n = int(input())
x, y = map(int,input().split())
m = int(input())
visited = []
graph = [[] for i in range(n+1)]
rank = [[] for i in range(n+1)]
for i in range(n+1):
    rank[i] = 0

for i in range(m):
    xn, yn = map(int, input().split())
    graph[xn].append(yn)
    graph[yn].append(xn)

print(rank)
print(graph)

