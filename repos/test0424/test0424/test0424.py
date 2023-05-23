
INF = float('inf')
M, N, K = map(int, input().split())
A = list(map(int, input().split()))

dp = [[INF] * (M+1) for _ in range(K+1)]
dp[0][M] = 0

for i in range(K):
    for j in range(M+1):
        dp[i+1][j] = min(dp[i+1][j], dp[i][j])
        if j+A[i] <= M:
            dp[i+1][j+A[i]] = min(dp[i+1][j+A[i]], dp[i][j] + 1)
        if j-A[i] >= 0:
            dp[i+1][j-A[i]] = min(dp[i+1][j-A[i]], dp[i][j] + 1)

        ans = dp[K][N] if dp[K][N] < INF else -1
print(ans)