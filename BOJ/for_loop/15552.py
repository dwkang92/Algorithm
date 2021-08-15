from sys import stdin

t = int(input())
for _ in range(t):
    a, b = list(map(int, stdin.readline().rstrip().split()))
    print(a+b)
