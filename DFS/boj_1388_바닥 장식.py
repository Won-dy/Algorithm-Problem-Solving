# https://www.acmicpc.net/problem/1388

def dfs(row, col, type):
    # global cnt
    # 범위 벗어나면 종료
    if not (0 <= row < N) or not (0 <= col < M):
        return False

    # 가로 판자
    if floor[row][col] == '-' and type == '-':
        floor[row][col] = 'x'  # 방문 표시
        dfs(row, col - 1, '-')  # 좌
        dfs(row, col + 1, '-')  # 우
        return True

    # 세로 판자
    if floor[row][col] == '|' and type == '|':
        floor[row][col] = 'x'  # 방문 표시
        dfs(row - 1, col, '|')  # 상
        dfs(row + 1, col, '|')  # 하
        return True

    return False


N, M = map(int, input().split())
floor = [list(map(str, input())) for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j, floor[i][j]):
            cnt += 1

print(cnt)