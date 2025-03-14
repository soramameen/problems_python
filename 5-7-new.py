if __name__ == '__main__':
    N, W = map(int, input().split())
    weight = []
    value = []
    for _ in range(N):
        w, v = map(int, input().split())
        weight.append(w)
        value.append(v)
    dp = [[0 for _ in range(W+1)] for _ in range(N+1)]
    for i in range(1, N+1):
        for w in range(W+1):
            dp[i][w] = dp[i-1][w]
            if w >= weight[i-1]:
                dp[i][w] = max(dp[i][w], dp[i-1][w-weight[i-1]]+value[i-1])
                # listなので，weight，valueを扱う際にはi-1を用いる
    print(dp)
