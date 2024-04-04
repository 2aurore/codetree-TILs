a = [int(input()) for __ in range(10)]

cnt = 0
for num in a :
    if num % 2 == 1:
        cnt += 1

print(cnt)