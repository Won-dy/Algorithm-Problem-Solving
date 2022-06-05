# https://www.acmicpc.net/problem/2217

N = int(input())
weight = [int(input()) for _ in range(N)]
weight.sort()

result = 0
for i in range(N):
    result = max(result, weight[i] * (N-i))

print(result)