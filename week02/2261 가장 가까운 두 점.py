import sys
input = sys.stdin.readline


def calc_distance(point1, point2):
    return (point1[0] - point2[0])**2 + (point1[1] - point2[1])**2


def divide_conquer(points, left, right):
    if right - left == 1:
        return calc_distance(points[left], points[right])  # 점이 두 개
    
    mid = (left + right) // 2

    min_distance = min(divide_conquer(points, left, mid), divide_conquer(points, mid, right))

    candidates = []

    # 중간 경계 영역
    for i in range(left, right + 1):
        if (points[mid][0] - points[i][0]) ** 2 < min_distance:
            candidates.append(points[i])

    candidates.sort(key=lambda x: x[1]) # y 기준으로 재정렬
    

    for i in range(len(candidates)-1):
        for j in range(i + 1, min(i+8, len(candidates))):
            if (candidates[j][1] - candidates[i][1]) ** 2 >= min_distance:
                break
            min_distance = min(min_distance, calc_distance(candidates[i], candidates[j]))
    
    return min_distance


point = []

n = int(input().strip())
points = [list(map(int, input().strip().split())) for _ in range(n)]

points.sort()


print(divide_conquer(points, 0, n - 1))