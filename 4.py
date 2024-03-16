N, M = [int(x) for x in input().split()]
m = [int(x) for x in input().split()]

dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        if m[i - 1] == j:
            dp[i][j] = 1
        elif m[i - 1] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = dp[i - 1][j]
            if (dp[i - 1][j - m[i - 1]] + 1) > 1:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - m[i - 1]] + 1) if (dp[i - 1][j] != 0) else dp[i - 1][j - m[i - 1]] + 1

print(dp[N][M])
