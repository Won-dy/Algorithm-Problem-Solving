import sys

input = sys.stdin.readline

arr = [0] * 1000001

n = int(input())
for i in map(int, input().split()):
    arr[i] += 1

m = int(input())
for j in map(int, input().split()):
    if arr[j] != 0:
        print('yes', end=' ')
    else:
        print('no', end=' ')