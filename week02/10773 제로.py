k = int(input())

stack = []

for _ in range(k):
    c = int(input())
    if c == 0:
        stack.pop()
    else:
        stack.append(c)

print(sum(stack))