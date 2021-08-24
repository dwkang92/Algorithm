# 이스케이프 문자
print("hello world")
print("Hello\nworld")  # \n: 줄바꿈
print("Hello\tWorld")  # \t: 탭
print("Hello\bWorld")  # \b: 백스페이스. 이 경우 b가 지워짐.
print("\000")  # Null문자
print("\\Hello world\\")  # \\ '\'


# 문자열 안에 따옴표를 포함하는 경우, 이스케이프 문자를 사용.
print("Hello world")  # Hello world

print("\"Hello world\"")  # "Hello world"

print('Hello world')  # Hello world

print('\'Hello world\'')  # 'Hello world'
