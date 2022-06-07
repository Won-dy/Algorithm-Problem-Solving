# https://youtu.be/7C9RgOcvkvo

def dfs(row, col):
    if ice[row][col] == 0:
        ice[row][col] = 1

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        for k in range(4):
            next_row = row + dx[k]
            next_col = col + dy[k]

            if 0 <= next_row < N and 0 <= next_col < M:
                dfs(next_row, next_col)

        return True

    return False


N, M = map(int, input().split())
ice = [list(map(int, input())) for _ in range(N)]

result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j):
            result += 1

print(result)