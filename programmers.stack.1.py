from math import ceil

def solution(progresses, speeds):
    X = []
    count = 0
    maxnum = ceil((100 - progresses[0])/speeds[0])

    for i in range(len(speeds)):
        Time = ceil((100 - progresses[i]) / speeds[i])

        if maxnum < Time:
            maxnum = Time
            X.append(count)
            count = 1
        else:
            count += 1

        if i == len(speeds)-1:
            X.append(count)

    return print(X)

P = [93, 30, 55]
S = [1, 30, 5]

solution(P,S)
