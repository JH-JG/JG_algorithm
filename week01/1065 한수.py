def is_hansu(num):
    n = str(num)
    if len(n) == 1:
        return True
    
    equal = int(n[0]) - int(n[1])

    for i in range(1, len(n) - 1):
        if equal != int(n[i]) - int(n[i+1]):
            return False

    return True


n = int(input())
cnt = 0

for i in range(1, n+1):
    if is_hansu(i):
        cnt += 1

print(cnt)