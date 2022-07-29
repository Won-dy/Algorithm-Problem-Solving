# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    s = list(s)
    stack = [s.pop()]
    while s:
        if stack and stack[-1] == s[-1]:  # 짝이 맞으면
            s.pop()
            stack.pop()
        else:  # 짝이 맞지 않거나 스택이 비어있으면
            stack.append(s.pop())  # 스택에 추가

    return 1 if not stack else 0


print(solution('baabaa'))  # 1
print(solution('cdcd'))  # 0