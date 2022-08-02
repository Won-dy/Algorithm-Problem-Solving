# https://school.programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for crs in course:  # 코스를 구성하는 단품메뉴들의 갯수 별
        comb = []  # 코스 구성하는 메뉴 조합
        for order in orders:  # 주문한 단품메뉴들
            comb += combinations(sorted(order), crs)

        order_comb = Counter(comb)  # 코스 구성하는 메뉴 조합의 주문 수
        if not order_comb:  # 메뉴를 crs개 이상 주문한 손님이 없을 때
            continue

        max_ = order_comb.most_common(1)[0][1]  # 가장 많이 함께 주문된 횟수
        if max_ >= 2:
            menu_comb = list(filter(lambda x: x[1] == max_, order_comb.items()))  # 코스 요리 메뉴 후보만 필터링
            for comb in menu_comb:
                answer.append(''.join(comb[0]))

    return sorted(answer)


print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))  # ["AC", "ACDE", "BCFG", "CDE"]
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))  # ["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))  # ["WX", "XY"]