# https://school.programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0

    d.sort()
    for price in d:
        budget -= price  # 예산 차감
        if budget >= 0:  # 예산이 남으면
            answer += 1  # 카운트
        else:
            break

    return answer


print(solution([1, 3, 2, 5, 4], 9))  # 3
print(solution([2, 2, 3, 3], 10))  # 4