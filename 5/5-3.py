"""
    緩和という考えかたを使って解く．
    dp[3] がチャンピオンでdp[2]+1やdp[1]+4などの挑戦者と戦い，
    チャンピオンを更新していくイメージ
    c++ではchmin関数を作るがpythonではminメソッドを使うほうが一般的．
"""

from typing import List


def frog(N: int, h: List[int]) -> int:
    dp = [2000000000]*N
    dp[0] = 0
    if N >= 2:
        for i in range(1, N):
            # battle1(inf vs from i-1)
            dp[i] = int(min(dp[i], dp[i-1]+abs(h[i]-h[i-1])))
            print(dp)
            if i >= 2:
                # battle2(inf vs from i-2)
                dp[i] = int(min(dp[i], dp[i-2]+abs(h[i]-h[i-2])))
                print(dp)
    return dp[N-1]


if __name__ == "__main__":
    N = int(input())
    h = list(map(int, input().split()))
    print(N, h)
    print(f'{frog(N, h)}')
