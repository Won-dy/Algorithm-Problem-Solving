# https://school.programmers.co.kr/learn/courses/30/lessons/92334

def solution(id_list, report, k):
    report = set(report)  # 중복 신고 제거

    singo_cnt_dict = {x: 0 for x in id_list}  # 유저별 신고된 횟수 초기화

    # 유저별 신고된 횟수 갱신
    for rpt in report:
        singo_cnt_dict[rpt.split(" ")[1]] += 1

    answer = [0] * len(id_list)

    for rpt in report:
        if singo_cnt_dict[rpt.split(" ")[1]] >= k:  # 정지된 아이디를 신고했으면
            answer[id_list.index(rpt.split(" ")[0])] += 1  # 메일 받은 횟수 카운트

    return answer


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"], 2))  # [2, 1, 1, 0]
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))  # [0, 0]