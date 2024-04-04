a, b = map(int, input().split())

sum_v = 0
if a > b :
    arr = range(b, a+1)
else :
    arr = range(a, b+1)
    
for i in arr:
    if i % 5 == 0:
        sum_v += i

print(sum_v)