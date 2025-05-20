n = int(input())

li = list(map(int, input().split()))

def perm(arr, n):
    result = []
    if n > len(arr):
        return result
    
    if n == 1:
        for i in arr:
            result.append([i])
    elif n > 1:
        for i in range(len(arr)):
            ans = [i for i in arr]
            ans.remove(arr[i])
            for p in perm(ans, n-1):
                result.append([arr[i]]+p)
    
    return result

results = []
for nums in perm(li, n):
    add = 0
    for i in range(n-1):
        add += abs(nums[i] - nums[i + 1])
    results.append(add)

print(max(results))