# https://www.acmicpc.net/problem/10610

def thirty(num_list):
    if '0' not in num_list:
        return -1

    add = 0
    for num in num_list:
        add += int(num)

    if add % 3 != 0:
        return -1

    num_list.sort(reverse=True)
    return int(''.join(num_list))


print(thirty(list(input())))