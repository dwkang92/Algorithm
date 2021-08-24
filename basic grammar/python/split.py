# .split()함수는 문자열을 나눌 때 사용되어진다.
# 괄호안에 아무것도 넣지않으면 공백(띄어쓰기, 탭 등)을 기준으로 문자열을 나눈다.
# 나뉘어진 값은 리스트의 요소로 저장되는데, 분할된 문자의 개수만큼 각각을 변수로 지정하는 것도 가능하다.

test = 'Hello world : 헬로 월드'
print(test)
print(test.split())
print(test.split(sep=':'))
print(test.split(maxsplit=1))
print(test.split(maxsplit=2))
print(test.split(maxsplit=3))

# -- 출력값
# Hello world: 헬로 월드
# ['Hello', 'world', ':', '헬로', '월드']  # 기본값으로 분할
# ['Hello world ', ' 헬로 월드']  # ':'기준 분할
# ['Hello', 'world : 헬로 월드']  # 공백기준, 1번 분할
# ['Hello', 'world', ': 헬로 월드']  # 공백기준, 2번 분할
# ['Hello', 'world', ':', '헬로 월드']  # 공백기준, 3번 분할
