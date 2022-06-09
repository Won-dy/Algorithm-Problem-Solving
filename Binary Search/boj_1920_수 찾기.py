# https://www.acmicpc.net/problem/1920

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return 1

        if array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return 0


N = int(input())
A = list(map(int, input().split()))
M = int(input())
arr = list(map(int, input().split()))

A.sort()

for m in arr:
    print(binary_search(A, m, 0, N - 1))