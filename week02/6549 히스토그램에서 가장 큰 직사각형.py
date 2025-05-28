# import sys
# sys.setrecursionlimit(10**6)
# input=sys.stdin.readline

# def find_min_idx(heights, left, right):
#     min_idx = left
#     for i in range(left+1, right+1):
#         if heights[min_idx] > heights[i]:
#             min_idx = i
#     return min_idx


# def devide_conquer(heights, left, right):
#     if left == right:
#         return heights[left]
    
#     left_max = 0
#     right_max = 0
    
#     min_idx = find_min_idx(heights, left, right)

#     if min_idx > left:
#         left_max = devide_conquer(heights, left, min_idx-1)
    
#     if min_idx < right:
#         right_max = devide_conquer(heights, min_idx + 1, right)
    
#     center_max = heights[min_idx] * (right - left + 1)

#     return max(center_max, left_max, right_max)

# while True:
#     square = list(map(int, input().rstrip().split()))
#     if not square[0]:
#         break
#     n, heights = square[0], square[1:]

#     print(devide_conquer(heights, 0, n-1))


# 스택을 이용한 풀이 위에 코드는 정답이나 시간초과 나옴
while True:
    line = list(map(int, input().split()))
    n = line[0]
    if n == 0:
        break
    
    heights = line[1:]
    stack = []
    max_area = 0
    
    for i in range(n):
        while stack and heights[stack[-1]] > heights[i]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)
    
    while stack:
        h = heights[stack.pop()]
        w = n if not stack else n - stack[-1] - 1
        max_area = max(max_area, h * w)
    
    print(max_area)



# import sys
# input = sys.stdin.readline
# res = []

# def divide_and_conquer(histogram, start, end):
#     if end == start:
#         return histogram[end]
#     elif end - start == 1:
#         if histogram[end] < histogram[start]:
#             return max(2*histogram[end], histogram[start])
#         else:
#             return max(2*histogram[start], histogram[end])

#     mid = (start + end) // 2
#     left_area = divide_and_conquer(histogram, start, mid)
#     right_area = divide_and_conquer(histogram, mid+1, end)
#     left = mid-1
#     right = mid+1
#     mid_area = histogram[mid]
#     now_height = histogram[mid]
#     while start <= left and right <= end:
#         if histogram[left] < histogram[right]:
#             if histogram[right] < now_height:
#                 now_height = histogram[right]
#             mid_area = max(mid_area, now_height * (right - left))
#             right += 1
#         else:
#             if histogram[left] < now_height:
#                 now_height = histogram[left]
#             mid_area = max(mid_area, now_height * (right - left))
#             left -= 1
            
#     while start <= left:
#         if histogram[left] < now_height:
#             now_height = histogram[left]
#         mid_area = max(mid_area, now_height * (right - left))
#         left -= 1
#     while right <= end:
#         if histogram[right] < now_height:
#             now_height = histogram[right]
#         mid_area = max(mid_area, now_height * (right - left))
#         right += 1

#     return max(left_area, right_area, mid_area)



# res = []
# while True:
#     histogram = list(map(int, input().split()))
    
#     if histogram[0] == 0: break
    
#     n = histogram[0]
    
#     res.append(divide_and_conquer(histogram, 1, n))

    
# for i in res:
#     print(i)