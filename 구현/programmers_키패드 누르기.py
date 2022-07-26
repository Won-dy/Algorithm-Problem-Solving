# https://school.programmers.co.kr/learn/courses/30/lessons/67256

def solution(numbers, hand):
    answer = ''
    left_pos, right_pos = 10, 12
    for number in numbers:
        if number == 0:
            number = 11
        if number % 3 == 0:
            answer += 'R'
            right_pos = number
        elif number % 3 == 1:
            answer += 'L'
            left_pos = number
        else:
            right_distance = (abs(right_pos - number) // 3) + (abs(right_pos - number) % 3)  # 오른쪽 손가락부터의 거리
            left_distance = (abs(left_pos - number) // 3) + (abs(left_pos - number) % 3)  # 왼쪽 손가락부터의 거리

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