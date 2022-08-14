# https://school.programmers.co.kr/learn/courses/30/lessons/12910

def solution(arr, divisor):
    answer = [a for a in arr if a % divisor == 0]
    if len(answer) == 0:  # 나누어 떨어지는 수가 하나도 없을때
        return [-1]
    else:
        return sorted(answer)  # 오름차순 정렬 후 리턴


print(solution([5, 9, 7, 10], 5))  # [5, 10]
print(solution([2, 36, 1, 3], 1))  # [1, 2, 3, 36]
print(solution([3, 2, 6], 10))  # [-1]