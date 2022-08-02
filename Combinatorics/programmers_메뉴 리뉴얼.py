# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import defaultdict, Counter


def solution(orders, course):
    answer = []
    orders = list(map(lambda x: sorted(x), orders))  # 알파벳 오름차순 정렬

    for crs in course[::-1]:  # 코스를 구성하는 단품메뉴들의 갯수 별
        menu_dict = defaultdict(int)
        for order in orders:  # 주문한 단품메뉴들
            for comb in combinations(order, crs):  # 코스 구성하는 메뉴 개수 조합
                menu_dict[comb] += 1

        if not menu_dict:  # 메뉴를 crs개 이상 주문한 손님이 없을 때
            continue

        max_ = max(menu_dict.items(), key=lambda x: x[1])[1]  # 가장 많이 함께 주문된 횟수
        if max_ >= 2:
            menu_comb = list(filter(lambda x: x[1] == max_, menu_dict.items()))  # 코스 요리 메뉴 후보만 필터링
            for comb in menu_comb:
                answer.append(''.join(comb[0]))

    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))  # ["AC", "ACDE", "BCFG", "CDE"]
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))  # ["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))  # ["WX", "XY"]