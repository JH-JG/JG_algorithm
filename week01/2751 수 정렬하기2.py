import sys
input=sys.stdin.readline

n = int(input())

nums = []
for i in range(n):
    nums.append(int(input()))

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    
    mid = len(arr) // 2
    low_arr = merge_sort(arr[:mid])
    high_arr = merge_sort(arr[mid:])

    return merge(low_arr, high_arr)

def merge(low_arr, high_arr):
    merge_arr = []

    l = h = 0

    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merge_arr.append(low_arr[l])
            l += 1
        else:
            merge_arr.append(high_arr[h])
            h += 1
    merge_arr += low_arr[l:]
    merge_arr += high_arr[h:]

    return merge_arr

a = merge_sort(nums)

for i in a:
    print(i)
