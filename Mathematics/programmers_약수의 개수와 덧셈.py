# https://school.programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    answer = 0
    for i in range(left, right + 1):
        if int(i ** 0.5) == i ** 0.5:  # 제곱 수는 약수의 개수가 홀수
            answer -= i
        else:  # 약수의 개수가 짝수
            answer += i

    return answer


print(solution(13, 17))  # 43
print(solution(24, 27))  # 52