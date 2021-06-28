import sys
from collections import deque
sys.stdin = open("in.txt", "r")

def bfs(x,y,graph, rank):
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    queue = deque()
    queue.appendleft([x,y])

    while queue:
        node = queue.pop()
        x = node[0]
        y = node[1]

        for nx, ny in directions:
            dx = nx + x
            dy = ny + y

            if 0 <= dx < M and 0 <= dy < N:
                if graph[dy][dx] and not visited[dy][dx]:
                    visited[dy][dx] = True
                    queue.appendleft([dx,dy])
                    rank[dy][dx] = rank[y][x] + 1
    return

N, M = map(int, sys.stdin.readline().split())
graph = [[] * M for i in range(N)]
visited = [[False]*M for i in range(N)]
rank = [[0] * M for i in range(N)]

for y in range(N):
    cord = sys.stdin.readline()
    for x in range(M):
        graph[y].append(int(cord[x]))

bfs(0,0,graph, rank)
print(rank[N-1][M-1]+1)
