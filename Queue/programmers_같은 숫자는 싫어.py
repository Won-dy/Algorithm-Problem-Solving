# https://school.programmers.co.kr/learn/courses/30/lessons/12906

from collections import deque


def solution(arr):
    arr = deque(arr)
    answer = [arr.popleft()]
    while arr:
        n = arr.popleft()
        if answer[-1] != n:  # 연속적인 숫자가 아니면
            answer.append(n)

    return answer


print(solution([1, 1, 3, 3, 0, 1, 1]))  # [1,3,0,1]
print(solution([4, 4, 4, 3, 3]))  # [4,3]