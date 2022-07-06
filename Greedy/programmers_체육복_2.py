# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):  # 전체 학생 수, 도난 당한 학생 번호, 여벌 체육복 가져온 학생 번호
    answer = n - len(lost) + len(set(lost) & set(reserve))  # 수업 들을 수 있는 학생 수

    lost.sort()

    # 여벌 체육복을 가져온 학생이 체육복을 도난당했을때 중복 제거
    lost_ = set(lost) - set(reserve)  # 도난 당한 학생 번호에서 제거
    reserve_ = set(reserve) - set(lost)  # 여벌 체육복 가져온 학생 번호에서 제거

    for l in lost_:
        # 앞 번호 학생에게 빌리기
        if l - 1 in reserve_:
            answer += 1
            reserve_.remove(l - 1)
            continue
        # 뒷 번호 학생에게 빌리기
        if l + 1 in reserve_:
            answer += 1
            reserve_.remove(l + 1)

    return answer


print(solution(5, [2, 4], [1, 3, 5]))  # 5
print(solution(5, [2, 4], [3]))  # 4
print(solution(3, [3], [1]))  # 2