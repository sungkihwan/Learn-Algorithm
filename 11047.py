import sys
sys.stdin = open("in.txt", "r")

N, K = map(int, input().split())
list = []
count = 0

for i in range(N):
    x = int(input())
    list.append(x)

list.sort(reverse=True)

for i in list:
    if i > K:
        continue
    else:
        count += K // i
        K = K % i
    if K == 0:
        break

print(count)