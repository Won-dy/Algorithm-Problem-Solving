# https://school.programmers.co.kr/learn/courses/30/lessons/82612

def solution(price, money, count):
    charge = 0  # 이용료
    for n in range(1, count + 1):  # 타게 되는 횟수 만큼
        charge += price * n  # 이용 금액 누적

    return max(0, charge-money)  # 이용 금액과 가진 금액 비교


print(solution(3, 20, 4))  # 10