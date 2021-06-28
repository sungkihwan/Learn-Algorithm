import sys
sys.stdin = open("in.txt", "r")

N = int(input()) - 1

length = list(map(int,sys.stdin.readline().split()))
price = list(map(int,sys.stdin.readline().split()))
minvalue = price[0]
price.pop()
result = 0

for i in range(N):
    if i == 0:
        result += price[i]*length[i]
    else:
        if minvalue > price[i]:
            minvalue = price[i]
        result += minvalue*length[i]

print(result)
