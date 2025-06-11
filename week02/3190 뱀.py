from collections import deque

n = int(input())
k = int(input())
board = [[0]*(n+1) for _ in range(n+1)]

for _ in range(k):
    r, c = map(int, input().split())
    board[r][c] = 1  # 사과 위치

L = int(input())
turns = dict()
for _ in range(L):
    X, C = input().split()
    turns[int(X)] = C

# 우, 하, 좌, 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
direction = 0  # 처음엔 오른쪽
snake = deque()
snake.append((1, 1))
time = 0
r, c = 1, 1

while True:
    time += 1
    nr = r + dr[direction]
    nc = c + dc[direction]
    # 벽이나 자기 몸에 부딪히면 종료
    if not (1 <= nr <= n and 1 <= nc <= n) or (nr, nc) in snake:
        break
    snake.append((nr, nc))
    if board[nr][nc] == 1:
        board[nr][nc] = 0  # 사과 먹기
    else:
        snake.popleft()  # 꼬리 이동
    r, c = nr, nc
    if time in turns:
        if turns[time] == 'D':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4

print(time)

