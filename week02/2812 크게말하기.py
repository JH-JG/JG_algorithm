import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())

stack = []
num = input().strip()


for n in num:
    while stack and k > 0 and stack[-1] < n:
        stack.pop()
        k -= 1
    stack.append(n)

while k > 0 and stack:
    stack.pop()
    k -= 1

print(''.join(stack))
