# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    rank_dict = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}

    match_cnt = 0
    for l in lottos:
        if l in win_nums:
            match_cnt += 1

    return [rank_dict[match_cnt + lottos.count(0)], rank_dict[match_cnt]]


def solution2(lottos, win_nums):
    rank = [6, 6, 5, 4, 3, 2, 1]

    match_cnt = len(set(lottos) & set(win_nums))
    return [rank[match_cnt + lottos.count(0)], rank[match_cnt]]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))  # [3, 5]
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))  # [1, 6]
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))  # [1, 1]

print(solution2([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))  # [3, 5]
print(solution2([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))  # [1, 6]
print(solution2([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))  # [1, 1]