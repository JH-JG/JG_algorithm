'''
‘()’ 인 괄호열의 값은 2이다.
‘[]’ 인 괄호열의 값은 3이다.
‘(X)’ 의 괄호값은 2×값(X) 으로 계산된다.
‘[X]’ 의 괄호값은 3×값(X) 으로 계산된다.
올바른 괄호열 X와 Y가 결합된 XY의 괄호값은 값(XY)= 값(X)+값(Y) 로 계산된다.
'''
s = input()

temp = 1
result = 0
stack = []

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
        temp *= 2
    elif s[i] == '[':
        stack.append(s[i])
        temp *= 3
    elif s[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        if s[i-1] == '(':  # 직전이 열린 괄호인 경우
            result += temp
        stack.pop()
        temp //= 2
    elif s[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        if s[i-1] == '[':  # 직전이 열린 괄호인 경우
            result += temp
        stack.pop()
        temp //= 3

if stack:
    result = 0

print(result)