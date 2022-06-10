# https://www.acmicpc.net/problem/2667

from collections import deque


def bfs(x, y):
    global queue, group

    # 방문 안했던 집이면
    if map[x][y] == 1:
        queue.append((x, y))  # 큐에 삽입
        map[x][y] = 8  # 방문 표시

        group += 1  # 단지 수 카운트
        house.append(1)  # 집 수 초기화 및 카운트

    # 큐가 빌 때 까지
    while queue:
        row, col = queue.popleft()

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        # 상하좌우 탐색
        for k in range(4):
            nx = row + dx[k]
            ny = col + dy[k]
            if 0 <= nx < N and 0 <= ny < N and map[nx][ny] == 1:  # 범위 내이고 방문하지 않았다면
                queue.append((nx, ny))  # 큐에 삽입
                map[nx][ny] = 8  # 방문 표시
                house[group] += 1  # 집 수 카운트


N = int(input())
map = [list(map(int, input())) for _ in range(N)]
group = 0  # 단지 수
house = [0]  # 단지별 집의 수
queue = deque()

for i in range(N):
    for j in range(N):
        bfs(i, j)

house.sort()
print(group)
for i in range(1, group + 1):
    print(house[i])