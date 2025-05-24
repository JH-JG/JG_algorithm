n = int(input())

for _ in range(n):
    stack = []
    s = input()
    for c in s:
        if c == '(':
            stack.append(c)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if not stack: 
            print("YES")
        else:
            print("NO")
