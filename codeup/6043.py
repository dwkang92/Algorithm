f1 = float(input())
f2 = float(input())
c = print(f1/f2)
print(round(float(input(c)), 2))

# 위와 같은 코드보다는 아래 코드가 간단하다.
a, b = map(float, input().split())
print('%.3f' % round(a/b, 3))
