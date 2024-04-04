arr = [int(input()) for __ in range(10)]

cnt3 = 0
cnt5 = 0
for num in arr:
    if num % 3 == 0:
        cnt3 += 1
    if num % 5 == 0:
        cnt5 += 1

print(cnt3 , cnt5)