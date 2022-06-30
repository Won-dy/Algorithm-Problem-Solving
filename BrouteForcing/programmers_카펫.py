# https://programmers.co.kr/learn/courses/30/lessons/42842
from math import sqrt


def solution(brown, yellow):
    answer = []

    for row in range(1, int(sqrt(yellow)) + 1):
        if yellow % row == 0:
            col = yellow // row  # 가로

            if brown == ((row + 2) * (col + 2) - yellow):
                answer.append(col + 2)
                answer.append(row + 2)
                break

    return answer


print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))