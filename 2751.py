import sys
sys.stdin = open("in.txt", "r")

N = int(input())
Numbers = []

for i in range(N):
    Numbers.append(int(sys.stdin.readline().rstrip()))

Numbers.sort()

for i in Numbers:
    print(i)
