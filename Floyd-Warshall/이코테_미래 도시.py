# https://youtu.be/acqm9mM1P6o

import sys

input = sys.stdin.readline
INF = int(1e9)

N, M = map(int, input().split())
graph = [[INF] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for j in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][j] + graph[j][b])

distance = graph[1][K] + graph[K][X]

if distance >= INF:
    print(-1)
else:
    print(distance)