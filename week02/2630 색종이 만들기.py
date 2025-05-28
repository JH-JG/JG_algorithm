def cut(n, x, y):
    global white, blue
    color = paper[x][y] # 현재 x, y를 기준으로 영역의 색을 정함

    for i in range(x, x+n):
        for j in range(y, y+n):
            if paper[i][j] != color:
                half = n//2
                cut(half, x, y)
                cut(half, x + half, y)
                cut(half, x, y + half)
                cut(half, x + half, y + half)
                return
    
    if color == 1:
        blue += 1
    else:
        white += 1


n = int(input())
white = 0
blue = 0

paper = [list(map(int, input().split())) for _ in range(n)]

cut(n, 0, 0)

print(white)
print(blue)