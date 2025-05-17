def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

n = int(input())

nums = list(map(int, input().split()))
cnt = 0

for num in nums:
    if is_prime(num):
        cnt += 1

print(cnt)