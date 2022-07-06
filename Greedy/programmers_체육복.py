# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):  # 전체 학생 수, 도난 당한 학생 번호, 여벌 체육복 가져온 학생 번호
    answer = n - len(lost)  # 수업 들을 수 있는 학생 수

    lost.sort()

    # 여벌 체육복을 가져온 학생이 체육복을 도난당했을때
    student_lost_and_reserve = []
    for lst in lost:
        if lst in reserve:
            answer += 1  # 수업 들을 수 있는 학생 수 추가
            student_lost_and_reserve.append(lst)
            reserve.remove(lst)  # 여벌 체육복 가져온 학생 번호에서 제거

    # 도난 당한 학생 번호에서 제거
    for s in student_lost_and_reserve:
        lost.remove(s)

    for l in lost:
        # 앞 번호 학생에게 빌리기
        if l - 1 in reserve:
            answer += 1
            reserve.remove(l - 1)
            continue
        # 뒷 번호 학생에게 빌리기
        if l + 1 in reserve:
            answer += 1
            reserve.remove(l + 1)

    return answer


print(solution(5, [2, 4], [1, 3, 5]))  # 5
print(solution(5, [2, 4], [3]))  # 4
print(solution(3, [3], [1]))  # 2