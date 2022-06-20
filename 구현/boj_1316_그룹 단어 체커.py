# https://www.acmicpc.net/problem/1316

from string import ascii_lowercase

N = int(input())
word = [input() for _ in range(N)]

cnt = 0
for w in word:
    is_group_word = True

    alpha = dict()
    for a in ascii_lowercase:
        alpha[a] = 0

    for i in range(len(w)):
        # 처음 나온 알파벳이면
        if alpha[w[i]] == 0:
            alpha[w[i]] += 1

        else:  # 나왔던 알파벳이면
            if w[i] == w[i - 1]:  # 연속되는 알파벳이면
                alpha[w[i]] += 1
            else:  # 떨어진 알파벳이면
                is_group_word = False
                break

    if is_group_word:
        cnt += 1

print(cnt)