# https://youtu.be/2zjoKjt97vQ

S = input()

result = []
sum = 0

for s in S:
    if s.isalpha():
        result.append(s)
    else:
        sum += int(s)

result.sort()

if sum != 0:
    result.append(str(sum))

print(''.join(result))