# https://www.acmicpc.net/problem/14889

import sys
from itertools import combinations as c

input = sys.stdin.readline

N = int(input())
ability = [list(map(int, input().split())) for _ in range(N)]

combination = list(c(list(range(N)), N // 2))
combLen = len(combination)

ans = 200
for team in range(combLen // 2):

    statTeam = linkTeam = 0
    startComb = list(c(combination[team], 2))
    linkComb = list(c(combination[combLen - team - 1], 2))

    for player in startComb:
        statTeam += ability[player[0]][player[1]] + ability[player[1]][player[0]]

    for player in linkComb:
        linkTeam += ability[player[0]][player[1]] + ability[player[1]][player[0]]

    diff = abs(statTeam - linkTeam)
    ans = min(ans, diff)
print(ans)