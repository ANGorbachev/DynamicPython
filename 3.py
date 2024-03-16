N = int(input())
nom = [int(x) for x in input().split()]
S = int(input())

dp = [0.0] + [float('inf')] * S
for i in range(1, S + 1):
    for j in range(N):
        if i >= nom[j] and dp[i - nom[j]] + 1 < dp[i]:
            dp[i] = dp[i - nom[j]] + 1

if dp[S] == float('inf'):
    print("No solution")
else:
    answer = []
    while S > 0:
        for j in range(N):
            if S - nom[j] >= 0 and dp[S] == dp[S - nom[j]] + 1:
                answer.append(str(nom[j]))
                S -= nom[j]
                break

    print(" ".join(answer[::-1]))
