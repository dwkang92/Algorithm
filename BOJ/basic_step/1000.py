a, b = list(map(int, input().split()))
print(a+b)

# 혹은 아래 코드로 한꺼번에 출력이 가능하다.
# print()안에 sum(map(int, input().split()))이 들어가 있다.
# 이제껏 list(map(int, input().split()))에만 익숙해져 있었는데, 갈피를 잘 잡았다.
print(sum(map(int, input().split())))
