# https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    key_dict = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                4: (1, 0), 5: (1, 1), 6: (1, 2),
                7: (2, 0), 8: (2, 1), 9: (2, 2),
                '*': (3, 0), 11: (3, 1), '#': (3, 2)}
    answer = ''
    left_pos, right_pos = '*', '#'
    for number in numbers:
        if number == 0:
            number = 11
        if number % 3 == 0:  # 오른쪽 열
            answer += 'R'
            right_pos = number
        elif number % 3 == 1:  # 왼쪽 열
            answer += 'L'
            left_pos = number
        else:  # 가운데 열
            right_distance = abs(key_dict[right_pos][0] - key_dict[number][0]) + abs(key_dict[right_pos][1] - key_dict[number][1])  # 오른쪽 손가락부터의 거리
            left_distance = abs(key_dict[left_pos][0] - key_dict[number][0]) + abs(key_dict[left_pos][1] - key_dict[number][1])  # 왼쪽 손가락부터의 거리

            if right_distance < left_distance:  # 오른쪽 손가락이 더 가까우면
                answer += 'R'
                right_pos = number
            elif left_distance < right_distance:  # 왼쪽 손가락이 더 가까우면
                answer += 'L'
                left_pos = number
            else:  # 거리가 같다면
                if hand == "right":  # 오른손잡이면
                    answer += 'R'
                    right_pos = number
                else:
                    answer += 'L'
                    left_pos = number

    return answer


print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))  # "LRLLLRLLRRL"
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))  # "LRLLRRLLLRR"
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))  # "LLRLLRLLRL"