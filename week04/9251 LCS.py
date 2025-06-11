# str1 = input()
# str2 = input()

# dp = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]

# for i in range(1, len(str1)+1):
#     for j in range(1, len(str2)+1):
#         if str1[i-1] == str2[j-1]:
#             dp[i][j] = dp[i-1][j-1] + 1
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# print(dp[len(str1)][len(str2)])

str1 = input()
str2 = input()

# 올바른 크기로 DP 테이블 생성 (1-based indexing을 위해 +1)
dp = [[0] * (len(str1) + 1) for _ in range(len(str2) + 1)]

# 1부터 시작하여 경계 조건 처리
for i in range(1, len(str2) + 1):
    for j in range(1, len(str1) + 1):
        if str2[i-1] == str1[j-1]:  # 문자열은 0-based indexing
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[len(str2)][len(str1)])