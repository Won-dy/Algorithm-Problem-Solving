# https://www.acmicpc.net/problem/10162

T = int(input())

button = [300, 60, 10]

if T % 10 != 0:
    print(-1)
else:
    cnt = []
    for b in button:
        cnt.append(T // b)
        T %= b
    print(*cnt)

    # 풀이 2
    # for b in button:
    #     print(T // b, end=' ')
    #     T %= b