n= int(input())

result = ''
for i in range(n):
    if (i+1) % 2 == 0 or (i+1) % 3 == 0 :
        result += '1'
    else: 
        result += '0'
    result += ' '
print(result)