import sys
from collections import deque
sys.stdin = open("in.txt", "r")

def dfs(x ,y ,graph):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    stack = [[x,y]]
    cnt = 1
    while stack:
        node = stack.pop()
        x = node[0]
        y = node[1]

        for nx, ny in directions:
            dx = nx + x
            dy = ny + y
            if 0 <= dx < n and 0 <= dy < n:
                if graph[dy][dx] and not visited[dy][dx]:
                    visited[dy][dx] = True
                    cnt += 1
                    stack.append([dx,dy])

    return list.append(cnt)

def bfs(x, y, graph):
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    queue = deque()
    queue.appendleft([x,y])
    cnt = 1
    while queue:
        node = queue.pop()
        x = node[0]
        y = node[1]
        for nx, ny in directions:
            dx = nx + x
            dy = ny + y
            if 0 <= dx < n and 0 <= dy < n:
                if graph[dy][dx] and not visited[dy][dx]:
                    visited[dy][dx] = True
                    cnt += 1
                    queue.appendleft([dx, dy])
    return list.append(cnt)

n = int(input())
graph = [[] for _ in range(n)] * n
visited = [[False] * n for _ in range(n)]
cnt = 0
list = []

for i in range(n):
    x = sys.stdin.readline()
    for j in range(n):
        graph[i].append(int(x[j]))

for dy in range(n):
    for dx in range(n):
        if graph[dy][dx] and not visited[dy][dx]:
            visited[dy][dx] = True
            dfs(dx,dy,graph)
            cnt += 1

print(cnt)
list.sort()

for i in list:
    print(i)