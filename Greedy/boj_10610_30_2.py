# https://www.acmicpc.net/problem/10610

num = input()
num_count = [0] * 10
sum = 0

for i in range(10):
    cnt = num.count(str(i))
    num_count[i] = cnt
    sum += num_count[i] * i

if num_count[0] == 0:
    print(-1)
elif sum % 3 != 0:
    print(-1)
else:
    for i in range(10):
        print(str(9 - i) * num_count[9 - i], end='')