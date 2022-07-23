# https://school.programmers.co.kr/learn/courses/30/lessons/81301

def solution(s):
    dic = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    answer = ''
    alpha = ''  # 영문자 저장용 변수
    for c in s:
        if c.isalpha():  # 영어이면
            alpha += c  # 영문자 저장
            if alpha in dic:  # 영단어이면
                answer += str(dic[alpha])  # 숫자로 변경
                alpha = ''  # 영문자 초기화
        else:  # 숫자면 그대로
            answer += c

    return int(answer)


print(solution("one4seveneight"))  # 1478
print(solution("23four5six7"))  # 234567
print(solution("2three45sixseven"))  # 234567
print(solution("123"))  # 123