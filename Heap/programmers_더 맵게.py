# https://school.programmers.co.kr/learn/courses/30/lessons/42626
import heapq


def solution(scoville, K):
    heapq.heapify(scoville)

    answer = 0
    while True:
        first = heapq.heappop(scoville)  # 가장 작은 스코빌 지수
        if first >= K:  # 모든 음식의 스코빌 지수가 K 이상이면
            return answer
        if len(scoville) == 0:  # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없으면
            return -1
        second = heapq.heappop(scoville)  # 두번째로 작은 스코빌 지수
        heapq.heappush(scoville, first + (second * 2))  # 새로운 음식 만든 후 삽입
        answer += 1  # 섞은 횟수 카운트


print(solution([1, 2, 3, 9, 10, 12], 7))  # 2
print(solution([12, 3, 9, 2, 10, 1], 7))  # 2
