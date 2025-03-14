from typing import List


def knapsack(N: int, W: int, weight: List[int], value: List[int]) -> int:
    dp = [[0] * (W + 1) for _ in range(N + 1)]
    for i in range(1, N + 1):
        for w in range(W + 1):
            dp[i][w] = dp[i-1][w]  # 選ばない
            if w >= weight[i-1]:  # 選べるなら
                dp[i][w] = max(dp[i][w], dp[i-1][w - weight[i-1]] + value[i-1])
        print(f"i={i}: {dp[i]}")  # 各行の状態確認
    return dp[N][W]


if __name__ == "__main__":
    N, W = map(int, input().split())
    weight, value = [], []
    for _ in range(N):
        w, v = map(int, input().split())
        weight.append(w)
        value.append(v)
    print(knapsack(N, W, weight, value))
