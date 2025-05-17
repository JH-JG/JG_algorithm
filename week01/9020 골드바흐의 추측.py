def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input())

for i in range(n):
    num = int(input())

    if num % 2 == 0:
        a, b = num // 2, num // 2
    else:
        a, b = num // 2, num // 2 + 1
    
    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break
        a -= 1
        b += 1
