n = int(input())

nums = list(map(int, input().split()))
expr = list(map(int, input().split()))

max_result = -1000000000
min_result = 1000000000

'''
dfs 숫자는 인덱스로 받아오고
부호만 남았는지 여부 판단, 백트래킹
'''

def dfs(idx, result, plus, minus, mul, div):
    global max_result, min_result
    if idx == n:
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return max_result, min_result
    
    if plus > 0:
        dfs(idx + 1, result + nums[idx], plus - 1, minus, mul, div)
    if minus > 0:
        dfs(idx + 1, result - nums[idx], plus, minus - 1, mul, div)
    if mul > 0:
        dfs(idx + 1, result * nums[idx], plus, minus, mul - 1, div)
    if div > 0:
        if result < 0:
            dfs(idx + 1, -(-result // nums[idx]), plus, minus, mul, div - 1)
        else:
            dfs(idx + 1, result // nums[idx], plus, minus, mul, div - 1)


dfs(1, nums[0], expr[0], expr[1], expr[2], expr[3])

print(max_result)
print(min_result)