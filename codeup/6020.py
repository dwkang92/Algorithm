a = input()
print(a.replace("-", "", 1))

# 파이썬은 문자열 변경을 할 수 있는 replace 함수를 제공합니다.
# replace와 replaceAll이 나눠져있는 자바와 혼동될 때가 있어서 메모합니다.
# replace()의 사용 방법은 아래와 같습니다.
# replace(old, new, [count]) -> replace("찾을값", "바꿀값", [바꿀횟수]


a, b = input().split("-")
print(a, b, sep="")
