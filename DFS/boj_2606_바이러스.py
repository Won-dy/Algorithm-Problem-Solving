# https://www.acmicpc.net/problem/2606

import sys

input = sys.stdin.readline


def dfs(node):
    global result

    visited[node] = True
    result += 1

    for g in graph[node]:
        if not visited[g]:
            dfs(g)
            visited[g] = True


n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

result = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(result - 1)