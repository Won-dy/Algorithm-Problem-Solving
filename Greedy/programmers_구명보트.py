# https://school.programmers.co.kr/learn/courses/30/lessons/42885


def solution(people, limit):
    people.sort(reverse=True)

    answer = 0
    boats = []
    for p in people:
        if p > (limit // 2):  # 무게 제한의 절반 초과 몸무게 사람들끼리는 같이 타지 못하므로
            boats.append([p])  # 한 명씩 태우기
            answer += 1
        else:
            break

    for i, p in enumerate(people[len(boats):]):
        if boats[-1][0] + p <= limit:  # 마지막 보트에 탈 수 있으면
            boats[-1].append(p)  # 탑승
            boats.pop()  # 두 명 탔으므로 더이상 못탐
        else:  # 마지막 보트에 못 타면
            boats.append([p])  # 새로운 보트에 탑승
            answer += 1

    return answer


print(solution([70, 50, 80, 50], 100))  # 3
print(solution([70, 80, 50], 100))  # 3