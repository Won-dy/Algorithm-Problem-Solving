# https://school.programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque


def solution(maps):
    n = len(maps)  # 맵의 세로 칸의 개수
    m = len(maps[0])  # 맵의 가로 칸의 개수

    # 상하좌우 방향 벡터
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    que = deque()
    que.append((0, 0, 1))
    maps[0][0] = 0
    while que:
        x, y, count = que.popleft()  # 칸 좌표, 지나온 칸의 개수

        if x == n - 1 and y == m - 1:  # 상대 팀 진영에 도착했으면
            return count

        # 상하좌우 칸 탐색
        for i in range(4):
            next_x = x + dx[i]
            next_y = y + dy[i]

            if 0 <= next_x < n and 0 <= next_y < m and maps[next_x][next_y] != 0:  # 맵 내의 칸이고 벽이 아니면
                maps[next_x][next_y] = 0  # 방문한 칸 벽으로 표시
                que.append((next_x, next_y, count + 1))

    return -1


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))  # 11
print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))  # -1