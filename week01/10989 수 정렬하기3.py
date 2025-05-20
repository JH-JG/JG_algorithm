import sys
input=sys.stdin.readline

n = int(input())

f = [0] * 10001

for _ in range(n):
    num = int(input())
    f[num] += 1


for i in range(1, 10001):
    if f[i] != 0:
        for _ in range(f[i]):
            print(i)
