# https://school.programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    return s.lower().count('p') == s.lower().count('y')


print(solution("pPoooyY"))  # true
print(solution("Pyy"))  # false