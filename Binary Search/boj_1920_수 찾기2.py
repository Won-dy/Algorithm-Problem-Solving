# https://www.acmicpc.net/problem/1920

import sys

input = sys.stdin.readline

N = input()
A = set(input().split())
M = input()

for m in input().split():
    print(1 if m in A else 0)