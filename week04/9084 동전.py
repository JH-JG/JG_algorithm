t = int(input())

for _ in range(t):
    n = int(input())
    coins = list(map(int, input().split()))
    m = int(input())

    dp = [0] * (m + 1)
    dp[0] = 1 # 0원을 만들 수 있는 가지수는 1

    for coin in coins:
        for i in range(coin, m + 1):
            # 현재 만들 수 있는 가지수는 이전에 만들었던 가지수 + 현재 만들수 있는 가지수
            dp[i] += dp[i - coin]
    
    print(dp[-1])
