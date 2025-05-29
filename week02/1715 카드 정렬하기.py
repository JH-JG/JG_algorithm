import heapq
import sys

input = sys.stdin.readline

n = int(input())
min_heap = []
result = 0

for _ in range(n):
    heapq.heappush(min_heap, int(input()))

for i in range(n-1):
    num1 = heapq.heappop(min_heap)
    num2 = heapq.heappop(min_heap)
    heapq.heappush(min_heap, num1 + num2)

    result += num1 + num2

print(result)
