# https://youtu.be/2zjoKjt97vQ

N = int(input())
scary = list(map(int, input().split()))

scary.sort()

group_num = 0
count = 0

for s in scary:
    count += 1
    if count >= s:
        group_num += 1
        count = 0

print(group_num)