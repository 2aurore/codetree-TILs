r = int(input())

num = [int(input()) for __ in range(r)]

for n in num: 
    if n % 3 == 0 and n % 2 == 1: 
        print(n)