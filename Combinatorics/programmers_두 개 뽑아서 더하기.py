# https://school.programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations


def solution(numbers):
    answer = []
    for comb in combinations(numbers, 2):  # 두개의 수를 뽑아서
        answer.append(sum(comb))  # 더한다

    return sorted(set(answer))  # 중복되는 수는 제거 후 오름차순으로 담아 return 한다


print(solution([2, 1, 3, 4, 1]))  # [2,3,4,5,6,7]
print(solution([5, 0, 2, 7]))  # [2,5,7,9,12]