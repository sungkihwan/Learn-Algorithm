import heapq
import sys
sys.stdin = open("in.txt", "r")

def dikjstra(start):
    distances = {node : float('inf') for node in graph}
    queue = []
    heapq.heappush(queue,[distances[start], start] )
    while queue:
        now_dis, now_node = heapq.heappop(queue)

        if distances[now_node] < now_dis:
            continue

        for new_dis, new_node in graph[now_node].items():
            distance = now_dis + new_dis

graph = {'A' : {'B' : 8, 'C' : 5}, 'B' : {}, 'C' : {}}