n = int(input())
arr = [int(input()) for _ in range(n)]

sum_val = 0
for num in arr:
    sum_val += num

print(sum_val, round(sum_val / n, 1))