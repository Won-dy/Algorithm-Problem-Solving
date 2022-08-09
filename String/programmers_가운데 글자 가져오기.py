# https://school.programmers.co.kr/learn/courses/30/lessons/12903

def solution(s):
    len_s = len(s)  # 단어의 길이
    if len_s % 2 == 0:  # 단어의 길이가 짝수라면
        return s[len_s // 2 - 1] + s[len_s // 2]
    else:  # 단어의 길이가 홀수라면
        return s[len_s // 2]


print(solution("abcde"))  # "c"
print(solution("qwer"))  # "we"