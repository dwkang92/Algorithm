# else 는 if 없이 혼자 사용되지 않는다.
# 또한, else 다음에는 조건식이 없는 이유는? True(참)가 아니면 False(거짓)이기 때문에...
# 조건식의 평가 결과는 True 아니면 False 로 계산되기 때문이다.

# python 에서는 들여쓰기를 기준으로 코드블록을 구분하므로, 들여쓰기를 정확하게 해주어야 한다.
a, b, c = map(int, input().split())
if a % 2 == 0:
    print('even')
else:
    print('odd')
if b % 2 == 0:
    print('even')
else:
    print('odd')
if c % 2 == 0:
    print('even')
else:
    print('odd')
