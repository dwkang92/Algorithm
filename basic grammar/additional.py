def sum(a):
    return a + a


tmp = list(map(int, input().split()))

print(map(sum, tmp))
print(list(int(map(sum, tmp)))
