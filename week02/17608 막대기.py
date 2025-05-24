import sys
input = sys.stdin.readline
n = int(input().strip())
cnt = 1
stack = []

for _ in range(n):
    stack.append(int(input().strip()))

max_height = stack.pop()

while stack:
    tmp = stack.pop()
    if max_height < tmp:
        max_height = tmp
        cnt += 1

print(cnt)