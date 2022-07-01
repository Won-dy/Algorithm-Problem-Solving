# https://programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter


def solution(participant, completion):
    dic = Counter(participant)  # 이름별 참가자 수를 카운트

    for c in completion:  # 완주자이면 카운트를 1씩 감소
        dic[c] -= 1

    return [k for k, v in dic.items() if v == 1][0]  # 1 남은 이름이 미완주 선수


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))  # "leo"
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))  # "vinko"
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))  # "mislav"