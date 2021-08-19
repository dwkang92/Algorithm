lst = []
for i in range(9):
    lst.append(int(input()))

max = max(lst)
print(max)
mix = lst.index(max)
print(mix+1)
