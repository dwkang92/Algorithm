# map(int, xxx) = map함수를 이용하여 각각의 리스트요소에 int함수를 적용시켜라.
# input().split() = 입력된 값을 쪼개주는데, 그걸 리스트로 저장한다.
# map함수는 map 객체로 반환한다. 우리의 국적이 map나라의 국적이 되어버리는 격.
# 원래 갖고 있던 국적을 찾아줘야하는데, list라는 국적을 갖고 있었으니, 앞에 list로 감싸준다.
a, b = list(map(int, input().split()))
print(a % b)
