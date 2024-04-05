a = int(input())

sum_v = 0
# 자기 자신을 제외한 약수를 모두 더함
for i in range(1, a):
    if a % i == 0: 
        sum_v += i

print('P') if a == sum_v else print('N')