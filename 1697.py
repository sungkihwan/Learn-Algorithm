import sys
from collections import deque
sys.stdin = open("in.txt", "r")

def bfs():
    q = deque([x])
    while q:
        now = q.pop()
        if now == y:
            return arr[y]
        for next in (now-1, now+1, now * 2):
            if 0 <= next <MAX and not arr[next]:
                arr[next] = arr[now] + 1
                q.appendleft(next)

MAX = 100000
arr = [0] * MAX
x, y = map(int, input().split())

print(bfs())

