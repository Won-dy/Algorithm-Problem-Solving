# https://school.programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    # return A or B
    # - A, B 둘 다 참이면 A 를 출력
    # - A, B 둘 다 거짓이면 B 를 출력
    # - A, B 둘 중에 하나만 참이면 참인 값을 출력

    return sorted([a for a in arr if a % divisor == 0]) or [-1]


print(solution([5, 9, 7, 10], 5))  # [5, 10]
print(solution([2, 36, 1, 3], 1))  # [1, 2, 3, 36]
print(solution([3, 2, 6], 10))  # [-1]