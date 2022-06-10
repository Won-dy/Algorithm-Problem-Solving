# https://www.acmicpc.net/problem/2805

def binary_search(trees, start, end):
    result = 0
    while start <= end:
        total_hieght = 0

        mid = (start + end) // 2

        # 나무 자르기
        for tree in trees:
            if tree > mid:
                total_hieght += tree - mid

        # 집에 가져갈 수 있는 높이
        if total_hieght >= M:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result


N, M = map(int, input().split())
trees = list(map(int, input().split()))
start, end = 0, max(trees)

print(binary_search(trees, start, end))