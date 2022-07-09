# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/

def solution(N):
    # write your code in Python 3.6
    binary_presnt = []
    while N != 0:
        binary_presnt.append(N % 2)
        N //= 2

    pos = []
    for i in range(len(binary_presnt)):
        if binary_presnt[i] == 1:
            pos.append(i)

    result = 0
    for j in range(len(pos) - 1, 0, -1):
        result = max(result, (pos[j] - pos[j - 1] - 1))

    return result


# 입력
print(solution(int(input())))