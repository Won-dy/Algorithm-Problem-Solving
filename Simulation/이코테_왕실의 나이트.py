# https://youtu.be/2zjoKjt97vQ

# 풀이 1
position = input()

column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
col = int(column.index(position[0]) + 1)
row = int(position[1])

d_row = [1, 2, 2, 1, -1, -2, -2, -1]
d_col = [2, 1, -1, -2, -2, -1, 1, 2]

count = 0
for i in range(8):
    next_row = row + d_row[i]
    next_col = col + d_col[i]
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        count += 1

print(count)


# 풀이 2
position = input()

col = int(ord(position[0]) - ord('a')) + 1
row = int(position[1])

steps = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]

count = 0
for step in steps:
    next_row = row + step[0]
    next_col = col + step[1]
    if 1 <= next_row <= 8 and 1 <= next_col <= 8:
        count += 1

print(count)