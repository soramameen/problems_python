"""
    配る遷移形式でとく
    dp[i]が決まったときにdp[i+1]とdp[i+2]を更新する
"""

from typing import List


def frog(N: int, h: List[int]) -> int:
    dp = [2000000000]*N
    dp[0] = 0
    for i in range(0, N-1):
        # battle 1
        dp[i+1] = int(min(dp[i+1], dp[i]+abs(h[i+1]-h[i])))
        # battle 2
        if i+2 < N:
            dp[i+2] = int(min(dp[i+2], dp[i]+abs(h[i+2]-h[i])))
        print(dp)
    return dp[N-1]


if __name__ == "__main__":
    N = int(input())
    h = list(map(int, input().split()))
    print(N, h)
    print(f'{frog(N, h)}')
