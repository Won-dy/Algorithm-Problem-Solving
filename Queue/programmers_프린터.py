# https://programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque


def solution(priorities, location):
    answer = 0

    priorities_dq = deque()
    for i, p in enumerate(priorities):
        priorities_dq.append((p, i))  # (중요도, 문서 번호)

    while priorities_dq:  # 큐가 빌 때까지
        print_doc = priorities_dq.popleft()

        if any(d[0] > print_doc[0] for d in priorities_dq):  # 더 중요한 문서 존재
            priorities_dq.append(print_doc)  # 대기 목록 맨 뒤로 추가
        else:  # 더 중요한 문서 없으면
            answer += 1  # 출력 횟수 카운트
            # 현재 출력 문서가 내 문서이면 리턴
            if print_doc[1] == location:
                return answer


print(solution([2, 1, 3, 2], 2))  # 1
print(solution([1, 1, 9, 1, 1, 1], 0))  # 5