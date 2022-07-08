# https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/

def solution(A, K):
    len_A = len(A)

    # 빈 배열은 길이가 0이므로 ZeroDivisionError 주의
    if len_A == 0:
        return A

    K %= len_A

    result = [-1] * len_A
    for i in range(len_A):
        result[(i + K) % len_A] = A[i]

    return result


# 입력
print(solution([3, 8, 9, 7, 6], 3))  # [9, 7, 6, 3, 8]
print(solution([0, 0, 0], 1))  # [0, 0, 0]
print(solution([1, 2, 3, 4], 4))  # [1, 2, 3, 4]
print(solution([], 0))  # []