import sys

N = int(sys.stdin.readline())
1 <= N <= 1000000

num = list(map(int, sys.stdin.readline().split()))
num.sort()
print(num[0], num[N-1])
