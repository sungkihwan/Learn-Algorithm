import sys
from collections import deque

sys.stdin = open("in.txt", "r")

def bfs(x, y):
    directions = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    q = deque()
    q.appendleft([x, y])
    while q:
        node = q.pop()
        x = node[0]
        y = node[1]
        for nx, ny in directions:
            dx = nx + x
            dy = ny + y
            if 0<= dx <m and 0<= dy <m:
                if not visited[dy][dx]:
                    visited[dy][dx] = True
                    rank[dy][dx] = rank[y][x] + 1
                    q.appendleft([dx, dy])

N = int(input())

for _ in range(N):
    m = int(input())
    visited = [[False]*m for i in range(m)]
    rank = [[0]*m for i in range(m)]

    startx, starty = map(int,input().split())
    endx, endy = map(int,input().split())

    visited[starty][startx] = True
    bfs(startx, starty)
    print(rank[endy][endx])