A = int(input())
start = 1
plus = 6
room = 1
if A == 1:
    print(1)
else:
    while True:
        first = start + plus
        room += 1
        if A <= start:
            print(room)
            break
        plus += 6
