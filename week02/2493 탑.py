import sys
input = sys.stdin.readline

n = int(input().rstrip())
stack = []
razor = [0] * n

tower = list(map(int, input().rstrip().split()))


for i in range(len(tower)-1, -1, -1):
    while stack and stack[-1][1] <= tower[i]:
        idx, _ = stack.pop()
        razor[idx] = i + 1
    stack.append((i, tower[i]))


for i in range(n):
    print(razor[i], end=' ')