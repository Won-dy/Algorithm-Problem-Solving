# https://programmers.co.kr/learn/courses/30/lessons/77486

def give_money(now, amount, enroll_dict, prt_chld_dict):
    my_money = amount - amount // 10
    your_money = amount // 10

    # 원 단위에서 배분할 금액이 없을 때 or 최상단 부모일 때
    if your_money == 0 or now == '-':
        enroll_dict[now] += amount  # 본인이 모두 가짐
        return

    enroll_dict[now] += my_money  # 본인 것 가지고
    give_money(prt_chld_dict[now], your_money, enroll_dict, prt_chld_dict)  # 나머지 부모에게 분배


def solution(enroll, referral, seller, amount):
    answer = []
    enroll_dict = {'-': 0}
    for e in enroll:
        enroll_dict[e] = 0

    prt_chld_dict = dict()  # 자식: 부모
    for e, r in zip(enroll, referral):
        prt_chld_dict[e] = r

    for s, a in zip(seller, amount):
        give_money(s, a * 100, enroll_dict, prt_chld_dict)

    answer = list(enroll_dict.values())[1:]
    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["sam", "emily", "jaimie", "edward"],
               [2, 3, 5, 4]))