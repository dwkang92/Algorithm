# 파이썬에서 map 은 input().split() 으로 분리해서 변수에 넣을 때 유용하게 쓰일 수 있다.
# map(int,input().split()) 은 split 으로 분리된 문자를 int 형으로 바꾸어 변수에 넣어준다.
# 아래 답은 같지만, 조금 더 좋은 코드를 작성하게 되면 그 아래와 같다.
# a = int(input())
# b = int(input())
# print(a-b)
a, b = map(int, input().split())
print(a-b)
