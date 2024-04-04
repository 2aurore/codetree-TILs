n = int(input())

for i in range(1, n+1):
    num_str = str(i)
    if i % 3 == 0:
        print(0, end=' ')
    #숫자 안에 3,6,9있는지 확인
    elif ("3" in num_str or "6" in num_str or "9" in num_str):
        print(0, end=' ')
    else:
        print(i, end=' ')