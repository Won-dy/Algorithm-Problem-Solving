# https://youtu.be/acqm9mM1P6o

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())

distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]

# 통로에 대한 정보 입력
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))


def dijkstra(start):
    q = []
    # 시작 노드는 최단 경로가 0
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:  # 큐가 비어있지 않을 동안

        # 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)

        # 방문한 적 있으면 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우 갱신
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(c)

cnt, max_dist = 0, 0

for d in distance:
    if d != INF:
        cnt += 1
        max_dist = max(max_dist, d)

# 시작 노드는 제외 하므로 cnt - 1
print(cnt - 1, max_dist)