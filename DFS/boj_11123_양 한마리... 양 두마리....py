# https://www.acmicpc.net/problem/11123

import sys

sys.setrecursionlimit(10 ** 6)


def dfs(x, y):
    if not (0 <= x < H) or not (0 <= y < W):
        return False

    if grid[x][y] == '#':
        grid[x][y] = 'x'

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True

    return False


for _ in range(int(input())):
    cnt = 0
    H, W = map(int, input().split())
    grid = [list(map(str, input())) for _ in range(H)]

    for i in range(H):
        for j in range(W):
            if dfs(i, j):
                cnt += 1

    print(cnt)