n = int(input())

nums = list(map(int, input().split()))


s = 0
e = len(nums)
result = 0
arr = []

def binary_search(arr, n):
    s, e = 0, len(arr)
    m = (s + e) // 2

    while s < e:
        m = (s + e) // 2
        if arr[m] < n:
            s = m + 1
        else:
            e = m
    
    return s


for n in nums:
    idx = binary_search(arr, n)

    if idx >= len(arr):
        arr.append(n)
    else:
        arr[idx] = n

print(len(arr))