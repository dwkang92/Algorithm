# 숫자를 입력받고 반복문에서 사용할 변수 num을 지정합니다.
input_num = int(input())
num = input_num  # num 변수에 input_num을 지정

# 여기서부터 무한루프 코드를 작성할 것이다. 무한루프 코드를 구성하는 방법은 while True:이다.

# 카운트 되는 숫자는 0부터로 설정하고, while문 상단에서 sum_num과 new_num을 구한다.
cnt = 0
while True:
    sum_num = (num // 10) + (num % 10)  # 각 자릿수를 더한수
    new_num = ((num % 10) * 10) + (sum_num % 10)  # 새로 만들어지는 수
    cnt += 1  # 사이클 카운트
    if new_num == input_num:
        break
    num = new_num  # num 변수에 last_num을 지정
print(cnt)
