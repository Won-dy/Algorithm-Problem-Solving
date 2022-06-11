# https://www.acmicpc.net/problem/1260

def dfs(grph, node, vstd):
    vstd[node] = True  # 현재 노드를 방문 처리
    print(node, end=' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in grph[node]:
        if not vstd[i]:
            dfs(grph, i, vstd)
            vstd[i] = True


def bfs(grph, node, vstd):
    queue = deque([node])

    vstd[node] = True  # 현재 노드를 방문 처리

    while queue:
        now_node = queue.popleft()
        print(now_node, end=' ')

        for i in grph[now_node]:
            if not vstd[i]:
                queue.append(i)
                vstd[i] = True


from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    key, value = map(int, input().split())
    graph[key].append(value)
    graph[value].append(key)

for i in range(1, N + 1):
    graph[i].sort()

visited = [False] * (N + 1)
dfs(graph, V, visited)
print()
visited = [False] * (N + 1)
bfs(graph, V, visited)
