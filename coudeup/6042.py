# format(수, ".2f") 를 사용하면 원하는 자리까지의 정확도로 반올림 된 실수 값을 만들어 준다.
# 여기서 만들어진 값은 소수점 아래 3번째 자리에서 반올림한 값이다.
a = float(input())
print(format(a, ".2f"))

print(round(float(input()), 2))
