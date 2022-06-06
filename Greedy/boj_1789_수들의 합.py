# https://www.acmicpc.net/problem/1789

S = int(input())

i = 1
cnt = 0
while S != 0:
    S -= i
    cnt += 1

    if S <= i:
        break

    i += 1

print(cnt)