import heapq
import sys
input = sys.stdin.readline

n = int(input())
heap = []
position = []
answer = 0

for i in range(n):
    a, b = map(int, input().strip().split())
    s, e = min(a, b), max(a, b)
    position.append((s,e))

d = int(input())

position.sort(key=lambda x: x[1])

for s, e in position:
    if e - s > d:
        continue
    while heap and heap[0] < e - d:
        heapq.heappop(heap)
    heapq.heappush(heap, s)

    answer = max(answer, len(heap))

print(answer)