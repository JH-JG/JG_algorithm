nums = list(input().split('-'))

result = sum(map(int, nums[0].split('+')))

for i in range(1, len(nums)):
    n = sum(map(int,nums[i].split('+')))
    result -= n

print(result)