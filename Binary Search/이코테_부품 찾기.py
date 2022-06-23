import sys

input = sys.stdin.readline


def binary_search(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        # 중간 값이 타겟보다 크면 왼쪽 탐색
        elif arr[mid] > target:
            end = mid - 1
        # 중간 값이 타겟보다 작으면 오른쪽 탐색
        else:
            start = mid + 1

    return None


n = int(input())
store = list(map(int, input().split()))
store.sort()

m = int(input())
for r in map(int, input().split()):
    if binary_search(store, r, 0, n - 1) is None:
        print('no', end=' ')
    else:
        print('yes', end=' ')