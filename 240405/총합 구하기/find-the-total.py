a, b = map(int, input().split())

sum_v = 0
for n in range(a, b+1):
    if n % 6 == 0 and n % 8 != 0:
        sum_v += n

print(sum_v)