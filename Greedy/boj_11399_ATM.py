# https://www.acmicpc.net/problem/11399

N = int(input())
P = list(map(int, input().split()))

P.sort()

result = 0
now_sum = 0

# 풀이 1
for p in P:
    now_sum += p
    result += now_sum

# 풀이 2
# for i in range(N):
#     result += sum(P[0:i + 1])

print(result)


