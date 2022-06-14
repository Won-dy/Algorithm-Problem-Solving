# https://www.acmicpc.net/problem/11123

from collections import deque


def bfs(x, y):
    global cnt, queue

    if grid[x][y] == '#':
        queue.append((x, y))
        grid[x][y] = 'x'
        cnt += 1

    while queue:
        row, col = queue.popleft()
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = row + dx[i]
            ny = col + dy[i]
            if (0 <= nx < H) and (0 <= ny < W) and grid[nx][ny] == '#':
                queue.append((nx, ny))
                grid[nx][ny] = 'x'


for _ in range(int(input())):
    H, W = map(int, input().split())
    grid = [list(map(str, input())) for _ in range(H)]

    cnt = 0
    queue = deque()
    for i in range(H):
        for j in range(W):
            bfs(i, j)

    print(cnt)