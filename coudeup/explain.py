# This is used to fetch input from the user. In this case, we are expecting the user to provice a list of integers.
# input 함수는 사용자로부터 입력을 받는 함수이며, 해당 함수가 호출되면 사용자는 입력을 하게되며, 입력된 내용은 문자열로 반환한다.
a = input()
print(a)

b = input("사용자 입력: ")
print(b)

# strip() 함수: 문자열 앞뒤의 공백 또는 특별한 문자 삭제. 문자열로 변환해준다.
# strip() is used to create a Python list out of a string. If no delimiter is given, this breaks the string by spaces.
input().strip()

# split() 함수: 문자열 내부에 있는 공백, 문자열을 리스트로 변환해준다.
# split() is used to create a Python list out of a string. If no delimiter is given, this breaks the string by spaces.
input().split()

# 입력받은 값을 문자열 + 리스트형으로 만들어준다.
input().strip().split()

# map() takes two arguments. The first one is the method to apply, the second one is the data to apply it to.
# By this understanding, we can see this is doing nothing but typecasting every element of the list to an integer value.
# Since map returns the data type it was applied to, the list() method applied over map() is redundant.
# syntax = map(func, *iterables)
map(int, input().strip().split())
list(map(int, input().strip().split()))

# list() converts its argument to a list
