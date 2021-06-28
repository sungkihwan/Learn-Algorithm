import sys
sys.stdin = open("in.txt", 'r')

K, N  = map(int, input().split())
array = []
for _ in range(K):
    x = int(input())
    array.append(x)

start = 0
end = max(array)
length = 0

while start != end:
    mid = (start + end + 1) // 2
    number = 0

    for i in range(K):
        number += array[i] // mid

    if number >= N:
        start = mid
        length = mid
    else:
        end = mid - 1

print(end)








# n, m = map(int, input().split(' '))
# array = list(map(int, input().split(' ')))
#
# end = max(array)
# start = 0
# result = 0

# while start <= end:
#     mid = (start + end) // 2
#     total = 0
#     total = sum([i-mid if mid < i else 0 for i in array])
#
#     if total >= m:
#         start = mid + 1
#         result = mid
#     else:
#         end = mid - 1

