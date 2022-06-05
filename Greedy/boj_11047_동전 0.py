# https://www.acmicpc.net/problem/11047

N, K = map(int, input().split())
A = [int(input()) for _ in range(N)]

result = 0
for value in A[::-1]:
    result += (K // value)
    K %= value

print(result)