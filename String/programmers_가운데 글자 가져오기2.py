# https://school.programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    return s[(len(s) - 1) // 2:len(s) // 2 + 1]


print(solution("abcde"))  # "c"
print(solution("qwer"))  # "we"