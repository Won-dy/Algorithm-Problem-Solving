# https://programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque


def solution(progresses, speeds):
    answer = []
    day = 1
    cnt = 0
    while len(progresses) > 0:
        if (progresses[0] + day * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            day += 1
    answer.append(cnt)

    return answer


print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))