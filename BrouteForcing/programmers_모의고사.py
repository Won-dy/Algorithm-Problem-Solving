# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []

    scores = [0, 0, 0]
    ans1 = [1, 2, 3, 4, 5]
    ans2 = [2, 1, 2, 3, 2, 4, 2, 5]
    ans3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):

        # 수포자 1
        if ans1[i % 5] == answers[i]:
            scores[0] += 1

        # 수포자 2
        if ans2[i % 8] == answers[i]:
            scores[1] += 1

        # 수포자 3
        if ans3[i % 10] == answers[i]:
            scores[2] += 1

    max_ = max(scores)
    for i in range(3):
        if scores[i] == max_:
            answer.append(i + 1)

    return answer


print(solution([1, 2, 3, 4, 5]))  # [1]
print(solution([1, 3, 2, 4, 2]))  # [1, 2, 3]