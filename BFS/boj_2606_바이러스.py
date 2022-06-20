# https://www.acmicpc.net/problem/2606

import sys
from collections import deque

input = sys.stdin.readline


def bfs(node):
    global result

    queue = deque([node])
    visited[node] = True

    while queue:
        now = queue.popleft()
        result += 1

        for g in graph[now]:
            if not visited[g]:
                queue.append(g)
                visited[g] = True


n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

result = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)
print(result - 1)