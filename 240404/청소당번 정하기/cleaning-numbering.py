n = int(input())

room = 0
floor = 0
bath = 0

for i in range(1, n):
    if i % 2 == 0 and not(i % 3 == 0) and not(i % 12 == 0):
        room += 1
    elif i % 3 == 0 and not(i % 12 == 0):
        floor += 1
    elif i % 12 == 0:
        bath += 1

print(room, floor, bath)