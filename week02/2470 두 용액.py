'''
산성 용액 특성 = 양의 정수
알칼리성 = 음의 정수

혼합한 용액의 특성 값은 각 용액의 특성 값 합
0에 가까운 용액을 만들려 함
'''
n = int(input())
solution = list(map(int, input().split()))
solution.sort()

min_diff = float('inf')
result = (solution[0], solution[-1])

start = 0
end = n - 1

while start < end:
    s = solution[start] + solution[end]
    if abs(s) < min_diff:
        min_diff = abs(s)
        result = (solution[start], solution[end])
    
    if s < 0:
        start += 1
    elif s > 0:
        end -= 1
    else:
        break

print(result[0], result[1])