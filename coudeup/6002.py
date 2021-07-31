# 6002번 문제
# Hello World 출력하기
# 문자열 = String. 문자, 단어 등으로 구성된 문자들의 집합을 의미한다.
# 문자열을 만드는 데에는 총 4가지 방법이 있다.
# A. 큰따옴표로 양쪽 둘러싸기
# B. 작은 따옴표로 양쪽 둘러싸기
# C. 큰 따옴표 3개를 연속으로 써서 양쪽 둘러싸기.
# D. 작은 따옴표 3개를 연속으로 써서 양쪽 둘러싸기.
# 왜 4개씩이나 있을까...?
# 아래 예시를 보자.

# Example 1
# Python's favourite food is perl
print("Python's favourite food is perl")
# invalid syntax; Python이 문자열로 인식되어버렸기 때문에 오류가 뜸.
print('Python\'s favourite food is perl')
# 문자열에 큰따옴표 포함시키기
# 문자열을 작은따옴표로 둘러싸면 된다.
print('"Python is very easy." he says.')

# Additional ways to make a semicolon
# 이스케이프 코드
# 백슬래시 \를 사용해 작은따옴표와 큰따옴표를 문자열에 포함시키기. 백슬래시를 작은따옴표나 큰따옴표 앞에 삽입하면 백슬래시 뒤의 작은 따옴표 혹은 큰따옴표는 문자열을
# 둘러싸는 기호의 의미가 아니라 문자 그 자체르 뜻하게 된다.
# 별도 설명은 블로그 참조.

print("Hello World")
