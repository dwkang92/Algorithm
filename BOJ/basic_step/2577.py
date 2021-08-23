a, b, c = list(map(int, input().split()))

result = a * b * c
for i in str(result):  # i = 0 ~ 9 까지 이므로
    print(i)
