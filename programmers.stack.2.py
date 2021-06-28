# from collections import deque

# def solution(priorities, location):

#     X = deque()
#     Y = deque()
#     count = 0

#     for i in range(len(priorities)):
#         Y.append(i)
#         X.append(priorities[i])

#     while X:
#         x = X.popleft()
#         y = Y.popleft()

#         if not X:
#             count += 1
#             if y == location:
#                 return count
#         elif x >= max(X):
#             count += 1
#             if y == location:
#                 return count
#         else:
#             X.append(x)
#             Y.append(y)

from collections import deque

def solution(priorities, location):
    queue = deque((i, p) for i, p in enumerate(priorities))
    count = 0
    while True:
        X = queue.popleft()
        if any(X[1] < q[1] for q in queue):
            queue.append(X)
        else:
            count += 1
            if X[0] == location:
                return print(count)

P = [2, 1, 3, 2]
L = 0
solution(P,L)
