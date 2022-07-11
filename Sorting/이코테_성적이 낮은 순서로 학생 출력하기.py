'''
3
홍길동 80
이순신 95
곽두철 51
'''

n = int(input())
arr = []
for _ in range(n):
    data = input().split()
    arr.append((data[0], int(data[1])))

arr.sort(key=lambda x: x[1])

for a in arr:
    print(a[0], end=' ')