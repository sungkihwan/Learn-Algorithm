import sys
sys.stdin = open("in.txt","r")

N = int(input())
Numbers = []

for i in range(N):
    X = str(i)
    Num = i
    for y in X:
        Num += int(y)
    if Num == N:
        Numbers.append(i)

if len(Numbers) == 0:
    print(0)
else:
    print(Numbers[0])


