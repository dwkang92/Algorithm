# 첫번째로 내가 작성한 식에 문제는 없다.
# 단지, 입력을 언제까지 계속해야하는지? 계속하다가 입력이 틀렸을 경우는 어떻게 대응되어지는지? 에대한 설명이 부족했다.
# 다른 사람들의 풀이를 보니, Python에는 try-except라는 개념이 있었다. 해당 구문은 구문오류가 발생했을 때 해결 할 수 있는 코드이다.
# try - except 구문의 기본적인 구조는 try 구문 쪽에 에러가 발생할 가능성이 있는 코드를 작성하고 except 구문 쪽에 예외 발생 시 실행할 코드를 작성하는 것이다. 이렇게 try - except 구문으로 코드를 작성해두면 에러가 없을 때는 try 구문을 실행하고서 except를 지나쳐서 그다음 코드를 계속 진행해나가고 에러가 발생하면 except 구문을 실행시킨다.


# while True:
#     a, b = map(int, input().split())
#     print(a+b)


while True:
    try:
        a, b = map(int, input().split())
    except:
        break
    print(a+b)
