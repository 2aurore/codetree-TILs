a,b = map(int, input().split())

sum_v = 0
for n in range(a, b+1):
    if n % 2 == 0:
        sum_v += n

print(sum_v)