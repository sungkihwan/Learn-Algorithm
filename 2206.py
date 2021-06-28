import sys
from collections import deque
sys.stdin = open("in.txt", "r")

def bfs():
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    q = deque()
    q.appendleft([0,0])
    cnt = 0
    while q:
        node = q.pop()
        x = node[0]
        y = node[1]
        for nx, ny in directions:
            dx = nx + x
            dy = ny + y
            if 0<= dx < xmax and 0<= dy <ymax:
                if not graph[dy][dx] and not visited[dy][dx]:
                    visited[dy][dx] = True
                    q.appendleft([dx,dy])
                    rank[dy][dx] = rank[y][x] + 1
                elif graph[dy][dx] and not visited[dy][dx] and cnt < 1:
                    visited[dy][dx] = True
                    q.appendleft([dx,dy])
                    rank[dy][dx] = rank[y][x] + 1
                    cnt += 1

    return

ymax, xmax = map(int, input().split())
graph = [[] for _ in range(ymax)]
visited = [[False]*xmax for _ in range(ymax)]
rank = [[1]*xmax for _ in range(ymax)]

for y in range(ymax):
    cord = sys.stdin.readline()
    for i in range(xmax):
        graph[y].append(int(cord[i]))

bfs()

if rank[ymax-1][xmax-1] == 1:
    print(-1)
else:
    print(rank[ymax-1][xmax-1])
