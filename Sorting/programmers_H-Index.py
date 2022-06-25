# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    answer = 0
    n = len(citations)
    citations.sort()

    for h in range(n, 0, -1):
        cnt = len(list(filter(lambda x: x >= h, citations)))  # h번 이상 인용된 논문 수
        if cnt >= h:  # h번 이상 인용된 논문이 h편 이상
            return h

    return answer


print(solution([3, 0, 6, 1, 5]))