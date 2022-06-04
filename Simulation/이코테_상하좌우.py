# https://youtu.be/2zjoKjt97vQ
N = int(input())
plan = list(map(str, input().split()))

direction = {
    'R': (0, 1),
    'L': (0, -1),
    'U': (-1, 0),
    'D': (1, 0)
}

position = [1, 1]

for p in plan:
    nextX = position[0] + direction[p][0]
    nextY = position[1] + direction[p][1]
    if 0 < nextX <= N and 0 < nextY <= N:
        position = [nextX, nextY]

print(position[0], position[1])
