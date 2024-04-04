n= int(input())

result = ''
for i in range(1, n+1):
    if (i) % 2 == 0 or (i) % 3 == 0 :
        result += '1'
    else: 
        result += '0'
    result += ' '
print(result)