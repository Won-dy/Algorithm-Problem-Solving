# https://youtu.be/7C9RgOcvkvo

from collections import deque


def bfs(row, col):
    global queue, result

    if ice[row][col] == 0:
        queue.append((row, col))
        ice[row][col] = 1
        result += 1

    while queue:
        x, y = queue.popleft()

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for k in range(4):
            next_row = x + dx[k]
            next_col = y + dy[k]

            if 0 <= next_row < N and 0 <= next_col < M and ice[next_row][next_col] == 0:
                queue.append((next_row, next_col))
                ice[next_row][next_col] = 1


N, M = map(int, input().split())
ice = [list(map(int, input())) for _ in range(N)]

queue = deque()
result = 0
for i in range(N):
    for j in range(M):
        bfs(i, j)

print(result)