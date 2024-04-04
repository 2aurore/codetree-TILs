a, b = map(int, input().split())

cnt = 0
sum_v = 0
for num in range(a, b+1):
    if num % 5 == 0 or num % 7 == 0:
        cnt += 1
        sum_v += num

print(sum_v, round(sum_v/cnt, 1))