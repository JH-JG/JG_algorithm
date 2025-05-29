import sys
import heapq
input = sys.stdin.readline


n = int(input().strip())

max_heap = [] # 최대힙 중간 값보다 작은 값 저장
min_heap = [] # 최소힙 중갑 값보다 큰 값 저장


for _ in range(n):
    num = int(input())
    # max_heap에 먼저 넣음
    if not max_heap or num <= -max_heap[0]:
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)

    # 두 힙의 크기 차이가 2 이상이면 조정
    if len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    elif len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))

    print(-max_heap[0])

# for _ in range(n):
#     heapq.heappush(max_heap, -int(input()))

#     if len(max_heap) - len(min_heap) > 1:
#         heapq.heappush(min_heap, -heapq.heappop(max_heap))

#     elif len(min_heap) - len(max_heap) > 1:
#         heapq.heappush(max_heap, -heapq.heappop(min_heap))


#     print(-max_heap[0])
