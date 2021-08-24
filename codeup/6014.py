# [기초-입출력]실수 1개 입력받아 3번출력하기
# range (start, stop, step)
# 마지막 인자 step은 숫자의 간격을 나타낸다.
# range() 함수의 결과는 반복가능하므로 for문을 사용해 출력할 수 있다.
# i.e. range(0, 20, 2) ... 0, 2, 4, 6, 8, 10, 12, 14, 16, 18
# i.e. range(20, 0, -2) ... 20, 18, 16, 14, 12, 10, 8, 6, 4, 2
a = float(input())
for i in range(3):
    print(a)
