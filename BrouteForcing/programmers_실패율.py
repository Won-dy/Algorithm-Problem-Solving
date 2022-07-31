# https://school.programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    fail_rate = dict()
    remain_cnt = len(stages)  # n 스테이지에 도전한 사람 수
    for stage_num in range(1, N + 1):
        no_clear = stages.count(stage_num)  # 현재 스테이지에서 클리어 못한 사람 수
        if remain_cnt != 0:
            fail_rate[stage_num] = (no_clear / remain_cnt)
        else:
            fail_rate[stage_num] = 0
        remain_cnt -= no_clear

    fail_rate = sorted(fail_rate.items(), key=lambda x: x[1], reverse=True)

    return [a[0] for a in fail_rate]


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))  # [3,4,2,1,5]
print(solution(4, [4, 4, 4, 4, 4]))  # [4,1,2,3]