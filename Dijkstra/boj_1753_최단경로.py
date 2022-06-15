# https://www.acmicpc.net/problem/1753

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))  # 큐에 (거리, 노드) 정보 삽입

    while q:
        dist, now = heapq.heappop(q)  # 최단 거리 꺼내기

        # 방문한 정점이면 무시
        if distance[now] < dist:
            continue

        for i in graph[now]:
            # 현재 노드를 거치는 경로가 더 짧으면 갱신
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 입력
v, e = map(int, input().split())
k = int(input())

distance = [INF] * (v + 1)
graph = [[] for _ in range(v + 1)]
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 다익스트라 알고리즘 실행
dijkstra(k)

# 출력
for d in distance[1:]:
    if d == INF:
        print("INF")
    else:
        print(d)