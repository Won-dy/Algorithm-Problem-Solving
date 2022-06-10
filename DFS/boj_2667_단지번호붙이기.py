# https://www.acmicpc.net/problem/2667


def dfs(x, y):
    global group, cnt
    # 방문 안했던 집이면
    if map[x][y] == 1:
        # map[x][y] = group  # 방문 표시 단지 명으로
        map[x][y] = 0  # 방문 표시
        cnt += 1  # 집의 수 세기

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        # 상하좌우 탐색
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < N:  # 범위 내이면
                dfs(nx, ny)
        return True

    # 방문했던 집이면 무시
    return False


N = int(input())
map = [list(map(int, input())) for _ in range(N)]
group, cnt = 0, 0  # 단지 수, 집의 수
house = []  # 단지별 집의 수

for i in range(N):
    for j in range(N):
        if dfs(i, j):
            group += 1
            house.append(cnt)
            cnt = 0

house.sort()
print(group)
for i in range(group):
    print(house[i])
