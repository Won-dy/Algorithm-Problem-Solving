# https://www.acmicpc.net/problem/1182

from itertools import combinations as cb

N, S = map(int, input().split())
nums = list(map(int, input().split()))

cnt = 0
for i in range(1, N + 1):
    for j in list(cb(nums, i)):
        if sum(j) == S:
            cnt += 1

print(cnt)