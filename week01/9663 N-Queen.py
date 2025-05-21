n = int(input())
cnt = 0
col = [False] * n
diag1 = [False] * (2 * n - 1)   # / 대각선
diag2 = [False] * (2 * n - 1)   # \ 대각선

def n_queens(row):
    global cnt
    if row == n:
        cnt += 1
        return
    for c in range(n):
        if not col[c] and not diag1[row + c] and not diag2[row - c + n - 1]:
            col[c] = diag1[row + c] = diag2[row - c + n - 1] = True
            n_queens(row + 1)
            col[c] = diag1[row + c] = diag2[row - c + n - 1] = False

n_queens(0)
print(cnt)