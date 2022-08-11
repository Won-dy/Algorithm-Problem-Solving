# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):  # 두 지도 행별 탐색
        map_row = ''
        for d1, d2 in zip(format(a1, '0' + str(n) + 'b'), format(a2, '0' + str(n) + 'b')):  # 이진수로 변경
            # 모두 공백일 때 공백을, 하나라도 벽일 때 #을 표시
            map_row += ' ' if d1 == '0' and d2 == '0' else '#'
        answer.append(map_row)
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))  # ["#####","# # #", "### #", "# ##", "#####"]
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
# ["######", "### #", "## ##", " #### ", " #####", "### # "]