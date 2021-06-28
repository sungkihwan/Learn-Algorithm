import sys
from collections import deque
sys.stdin = open("in.txt", "r")

def dfs(start, graph):
    visited = []
    stack = [start]
    while stack:
        n = stack.pop()
        if n not in visited:
            stack.extend(graph[n])
            visited.append(n)
    return print(len(visited)-1)

# bfs 오류남 queue.pop(0)에서
def bfs(start, graph):
    queue = deque()
    queue.appendleft(start)
    visited = []
    while queue:
        n = queue.pop()
        if n not in visited:
            visited.append(n)
            queue.extend(graph[n])
    return print(len(visited)-1)

a = int(input())
n = int(input())
start = 1

graph = [[] for _ in range(a+1)]

for i in range(n):
    x,y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

dfs(start, graph)







