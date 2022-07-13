# https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    max_w, max_h = 0, 0

    # 가장 긴 세로와 가장 긴 가로 찾기
    for size in map(lambda x: sorted(x), sizes):  # 긴 모서리를 모두 세로 쪽으로 배치
        max_w = max(max_w, size[0])
        max_h = max(max_h, size[1])

    return max_w * max_h


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))  # 4000
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))  # 120
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))  # 133