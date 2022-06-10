# https://youtu.be/94RC-DsGMLo

N, M = map(int, input().split())
ricecake = list(map(int, input().split()))

start, end = 0, max(ricecake)
result = 0
while start <= end:
    tot_height = 0
    mid = (start + end) // 2

    for rc in ricecake:
        if rc > mid:
            tot_height += rc - mid

    if tot_height >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)
