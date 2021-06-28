from collections import deque

def solution(bridge_length, weight, truck_weights):

    trucks = deque()
    time = 0

    for i in range(len(truck_weights)):
        trucks.append(truck_weights[i])

    while trucks:
        x = deque()

        for j in range(len(trucks)):
            h = trucks.popleft()
            if x + h < weight and len(x) < bridge_length:
                x.append(h)
                time += 1
            else:
                break


    return


bl = 2
w = 10
tw = [7, 4, 5, 6]

solution(bl,w,tw)