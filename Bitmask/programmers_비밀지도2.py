# https://school.programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []
    for a1, a2 in zip(arr1, arr2):  # 두 지도 행별 탐색
        map_row = format(a1 | a2, 'b').zfill(n)  # OR 비트 연산자 사용 후 이진수로 변환후 왼쪽 공백 0으로 채우기
        map_row = map_row.replace('1', '#')
        map_row = map_row.replace('0', ' ')
        answer.append(map_row)
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))  # ["#####","# # #", "### #", "# ##", "#####"]
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
# ["######", "### #", "## ##", " #### ", " #####", "### # "]