# https://school.programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations


def solution(nums):
    # 소수 판별
    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        else:
            return True

    answer = 0
    prime_dic = dict()  # 소수 판별 결과
    for num in combinations(nums, 3):
        sum_ = sum(num)  # 세 수의 합
        if sum_ in prime_dic:  # 이미 소수 판별한 적 있는 수이면
            if prime_dic[sum_]:
                answer += 1  # 카운트
        else:
            if is_prime(sum_):  # 소수이면
                prime_dic[sum_] = True
                answer += 1  # 카운트
            else:  # 소수 아니면
                prime_dic[sum_] = False

    return answer


print(solution([1, 2, 3, 4]))  # 1
print(solution([1, 2, 7, 6, 4]))  # 4