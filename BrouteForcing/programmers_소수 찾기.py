# https://programmers.co.kr/learn/courses/30/lessons/42839
from itertools import permutations
from math import sqrt


def is_prime_num(num):
    if num <= 1:
        return False
    # for i in range(2, num):
        # for i in range(2, int(sqrt(num))):
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


def solution(numbers):
    prime = []
    for i in range(1, len(numbers) + 1):
        for n in list(set(permutations(numbers, i))):
            print('n=', n)
            print(int(''.join(n)))
            if is_prime_num(int(''.join(n))):
                print('소수', int(''.join(n)))
                prime.append(int(''.join(n)))

    print(prime)
    answer = len(set(prime))
    return answer


print(solution("17"))
print(solution("011"))
