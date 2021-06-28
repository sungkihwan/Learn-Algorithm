import sys
sys.stdin = open("in.txt", "r")

N=[1]

while N:
    N=list(map(int, sys.stdin.readline().split()))

    if len(N) == 1 and N[0] == 0:
        break

    print(N)

