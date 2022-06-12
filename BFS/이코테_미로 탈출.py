# https://youtu.be/7C9RgOcvkvo

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        print(x, ',', y)

        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로찾기 공간을 벗어난 경우 또는 시작점인 경우 무시
            if not (0 <= nx < N) or not (0 <= ny < M) or (nx == 0 and ny == 0):
                continue

            # 괴물인 경우 무시
            if miro[nx][ny] == 0:
                continue

            # 처음 방문하는 경우 최단 거리 기록
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx, ny))

    # 도착점 까지의 최단 거리 반환
    return miro[N - 1][M - 1]


from collections import deque

N, M = map(int, input().split())
miro = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))
for m in miro:
    print(m)
