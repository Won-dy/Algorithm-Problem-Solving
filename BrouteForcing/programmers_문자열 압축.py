# https://school.programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    len_s = len(s)
    answer = len_s

    for cut in range(1, len_s // 2 + 1):
        zip_str = ''  # 압축된 문자열
        remain = 0  # 남은 문자열 시작 인덱스
        repeat_cnt = 1  # 문자열 반복 횟수
        last_str = ''  # 마지막 문자
        for i in range(cut, len_s - cut + 1, cut):
            remain = i + cut
            cut_s1 = s[i - cut:i]
            cut_s2 = s[i:i + cut]
            last_str = cut_s2  # 마지막 문자
            if cut_s1 == cut_s2:  # 반복 되면
                repeat_cnt += 1
            else:  # 반복 안되면
                zip_str += (str(repeat_cnt) if repeat_cnt > 1 else '') + cut_s1
                repeat_cnt = 1  # 문자열 반복 횟수 초기화
                continue

        # 마지막 문자 붙이기
        zip_str += (str(repeat_cnt) if repeat_cnt > 1 else '') + last_str

        # 남은 문자열 붙이기
        zip_str += s[remain:]

        answer = min(answer, len(zip_str))

    return answer


print(solution("aabbaccc"))  # 7  2a2ba3c
print(solution("ababcdcdababcdcd"))  # 9  2ababcdcd
print(solution("abcabcdede"))  # 8  2abcdede
print(solution("abcabcabcabcdededededede"))  # 14  2abcabc2dedede
print(solution("xababcdcdababcdcd"))  # 17  xababcdcdababcdcd

print(solution("a"))  # 1  a