import sys
input = sys.stdin.readline

n = int(input().strip())
circles = []
stack = []

points = [list(map(int, input().strip().split())) for _ in range(n)]

for x, r in points:
    circles.append([x-r, 1]) # 시작점
    circles.append([x+r, 2]) # 끝점

cnt = 1

circles.sort(key=lambda x: [x[0], -x[1]])


for circle in circles:
    if circle[1] == 1:
        stack.append(circle)
    else:
        outer_width = 0
        while stack:
            prev = stack.pop()
            if prev[1] == 1:
                width = circle[0] - prev[0]
                if outer_width == width:
                    cnt += 2
                else:
                    cnt += 1
                stack.append([width, 3])
                break

            elif prev[1] == 3:
                outer_width += prev[0]


print(cnt)
