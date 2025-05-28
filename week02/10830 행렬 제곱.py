import sys
input = sys.stdin.readline

def matrix_multiply(mat_a, mat_b):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += ((mat_a[i][k] * mat_b[k][j]) % 1000)

    return result


def matrix_pow(mat, b):
    if b == 1:
        return mat
    
    temp = matrix_pow(mat, b//2)

    if b % 2 == 0:
        return matrix_multiply(temp, temp)
    else:
        return matrix_multiply(matrix_multiply(temp, temp), mat)



n, b = map(int, input().strip().split())

mat = [list(map(int, input().strip().split())) for _ in range(n)]

result = matrix_pow(mat, b)

for i in range(n):
    for j in range(n):
        print(result[i][j] % 1000, end=' ')
    print()