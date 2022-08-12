# https://school.programmers.co.kr/learn/courses/30/lessons/17682

def solution(dartResult):
    if '10' in dartResult:
        dartResult = dartResult.replace('10', 'A')
        dartResult = ['10' if i == 'A' else i for i in dartResult]
    else:
        dartResult = list(dartResult)

    bonus = {'S': 1, 'D': 2, 'T': 3}
    score, options = [], []
    num = 0
    for i in range(1, len(dartResult)):
        try:  # 점수 구하기
            num = int(dartResult[i - 1])
        except ValueError:  # 옵션 적용
            # 옵션이 스타상일 때
            if dartResult[i] == '*' or dartResult[i] == '#':
                options.append((i // 3, dartResult[i]))  # (옵션의 순서, 옵션 내용)
        # 점수 계산
        if dartResult[i] in bonus:  # 보너스일 때
            score.append(num ** bonus[dartResult[i]])

    # 옵션 적용
    for option in options:
        sequnce, value = option
        # 옵션이 스타상일 때
        if value == '*':
            score[sequnce] *= 2
            if sequnce != 0:  # 첫 번째 기회에서 나온 것이 아닐때
                score[sequnce - 1] *= 2
        # 옵션이 아차상일 때
        elif value == '#':
            score[sequnce] *= -1

    return sum(score)


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