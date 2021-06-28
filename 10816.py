# import sys
# sys.stdin = open("in.txt", "r")
#
# N = int(input())
# Nlist = list(map(int, sys.stdin.readline().split()))
# Nlist.sort()
#
# M = int(input())
# Mlist = list(map(int,sys.stdin.readline().split()))
#
# def bianrysearch(start, end, M, cnt):
#     while start != end:
#         mid = (start + end - 1) // 2
#         number = Nlist[mid]
#
#         if number == M:
#             cnt += 1
#
#         if number <= M:
#             start = mid + 1
#         else:
#             end = mid
#     print(cnt)
#
# for i in range(M):
#     start = 0
#     end = max(Mlist)
#     cnt = 0
#     bianrysearch(start, end, Mlist[i], cnt)
