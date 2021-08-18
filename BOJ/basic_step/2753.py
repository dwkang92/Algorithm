# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.

year = int(input())

if year % 4 != 0:
    print('0')
elif year % 100 != 0:
    print('1')
elif year % 400 != 0:
    print('0')
else:
    print('1')


# 아니면 이런 방법도 있다. 문제에서 제시해주는 내용 그대로 코드를 짜버리는 방법.

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print('1')
else:
    print('0')
