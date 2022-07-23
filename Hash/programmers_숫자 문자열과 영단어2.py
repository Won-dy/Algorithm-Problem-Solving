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

    for eng, num in dic.items():
        s = s.replace(eng, num)

    return int(s)


print(solution("one4seveneight"))  # 1478
print(solution("23four5six7"))  # 234567
print(solution("2three45sixseven"))  # 234567
print(solution("123"))  # 123