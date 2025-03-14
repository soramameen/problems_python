"""
    ナップサック問題
    ナップサック問題 　N 個の品物があり，i(＝0, 1, ..., N－1) 番目の品物の重さは weighti，価値は valuei で与えられます． 　
    この N 個の品物から，重さの総和が W を超えないように，いくつか選びます．選んだ品物の価値の総和として考えられる最大値を求めてください．
    入力：
    4 10
    2 3
    4 5
    5 7
    3 4
"""

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
print(dp[N][W])
