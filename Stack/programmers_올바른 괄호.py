# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []
    for v in s:
        if v == '(':  # 열린 괄호이면
            stack.append(v)

        if v == ')':  # 닫힌 괄호이면
            if not stack:  # 스택이 비어있으면
                return False  # 올바르지 않은 괄호
            else:
                stack.pop()

    return len(stack) == 0


print(solution("()()"))  # true
print(solution("(())()"))  # true
print(solution(")()("))  # false
print(solution("(()("))  # false