# https://school.programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    answer = []
    if '10' in dartResult:
        dartResult = dartResult.replace('10', 'A')
        dartResult = ['10' if i == 'A' else i for i in dartResult]
    else:
        dartResult = list(dartResult)

    i = -1
    bonus = {'S': 1, 'D': 2, 'T': 3}
    for dr in dartResult:
        if dr in bonus:  # 보너스일 때
            answer[i] **= bonus[dr]
        elif dr == '*':  # 옵션이 스타상일 때
            answer[i] *= 2
            if i != 0:  # 첫 번째 기회에서 나온 것이 아닐때
                answer[i - 1] *= 2
        elif dr == '#':  # 옵션이 아차상일 때
            answer[i] *= (-1)
        else:  # 점수일 때
            answer.append(int(dr))
            i += 1

    return sum(answer)


print(solution('1S2D*3T'))  # 37	1^1 * 2 + 2^2 * 2 + 3^3
print(solution('1D2S#10S'))  # 9	1^2 + 2^1 * (-1) + 10^1
print(solution('1D2S0T'))  # 3	    1^2 + 2^1 + 0^3
print(solution('1S*2T*3S'))  # 23	1^1 * 2 * 2 + 2^3 * 2 + 3^1
print(solution('1D#2S*3S'))  # 5	1^2 * (-1) * 2 + 2^1 * 2 + 3^1
print(solution('1T2D3D#'))  # -4	1^3 + 2^2 + 3^2 * (-1)
print(solution('1D2S3T*'))  # 59	1^2 + 2^1 * 2 + 3^3 * 2

print(solution("10S1S0S*"))  # 12
print(solution("1S2D3T*"))  # 63
print(solution("1S2D*3T*"))  # 72
print(solution("1S*2D*3T*"))  # 74
print(solution("1S#2D*3T*"))  # 68