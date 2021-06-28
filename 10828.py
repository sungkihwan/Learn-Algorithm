import sys
sys.stdin = open("in.txt", "r")

from collections import deque
N = int(input())
q = deque()

for i in range(N):
    x = list(map(str, sys.stdin.readline().split()))
    if 'push' in x[0]:
        q.appendleft(x[1])
    elif 'pop' in x[0]:
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif 'size' in x[0]:
        print(len(q))
    elif 'empty' in x[0]:
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif 'top' in x[0]:
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
