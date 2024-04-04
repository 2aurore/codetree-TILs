# 변수 선언, 입력
n = int(input())

for _ in range(n):
    a = int(input())
    if a % 2 == 1 and a % 3 == 0:
        print(a)