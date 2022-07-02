# https://programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    answer = 0
    dic = {')': '(', ']': '[', '}': '{'}

    len_s = len(s)

    # 괄호 개수가 홀수이면
    if len_s % 2 != 0:
        return answer

    for i in range(len_s):
        rotate = s[i:] + s[:i]

        stack = []
        for j in range(len_s):

            if not stack:  # 스택이 비었으면
                stack.append(rotate[j])  # 스택에 괄호 삽입
                if rotate[j] in [')', ']', '}']:  # 첫 괄호가 닫힌 괄호라면
                    break
            else:  # 스택이 비지 않았으면
                prev = stack[-1]  # 전 괄호

                # 전 괄호가 닫힌 괄호면 또는 지금 괄호가 열린 괄호면
                if prev in [')', ']', '}'] or rotate[j] in ['(', '[', '{']:
                    stack.append(rotate[j])  # 스택에 괄호 삽입하고 다음으로
                    continue

                # 전 괄호가 열린 괄호이고 지금 괄호가 닫힌 괄호일때
                if dic[rotate[j]] == prev:  # 짝이면
                    stack.pop()  # 괄호 제거

        if not stack:  # 괄호가 모두 짝을 찾았으면
            answer += 1

    return answer


print(solution("[](){}"))  # 3
print(solution("}]()[{"))  # 2
print(solution("[)(]"))  # 0
print(solution("}}}"))  # 0