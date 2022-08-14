# https://school.programmers.co.kr/learn/courses/30/lessons/12915

def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))  # 인덱스 기준 정렬, 문자열 기준 정렬


print(solution(["sun", "bed", "car"], 1))  # ["car", "bed", "sun"]
print(solution(["abce", "abcd", "cdx"], 2))  # ["abcd", "abce", "cdx"]