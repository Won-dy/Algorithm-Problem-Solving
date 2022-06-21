# https://www.acmicpc.net/problem/6603

from itertools import combinations as comb

while True:
    k = 0
    S = []
    for i, v in enumerate(map(int, input().split())):
        if i == 0:
            k = v
        else:
            S.append(str(v))
    if k == 0:
        break

    for i in list(comb(S, 6)):
        print(' '.join(i))
    print()