arr = [int(input()) for _ in range(10)]

sum_v = 0
cnt = 0
for n in arr:
    if n >= 0 and n <= 200:
        sum_v += n
        cnt += 1

print(sum_v, round(sum_v / cnt, 1))