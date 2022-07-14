# https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution(nums):
    # 폰켓몬 종류별 마리 수 저장
    type_dic = dict()
    for num in nums:
        if num in type_dic:
            type_dic[num] += 1
        else:
            type_dic[num] = 1

    return min(len(nums) // 2, len(set(nums)))  # 고를 폰켓몬 수와 폰켓몬 종류 수 중 더 작은 수 리턴


print(solution([3, 1, 2, 3]))  # 2
print(solution([3, 3, 3, 2, 2, 4]))  # 3
print(solution([3, 3, 3, 2, 2, 2]))  # 2