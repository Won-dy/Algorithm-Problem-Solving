# https://school.programmers.co.kr/learn/courses/30/lessons/87389

def solution(n):
    for i in range(1, n):
        if n % i == 1:
            return i


print(solution(10))  # 3
print(solution(12))  # 11