"""
　図5.1のように N 個の足場があって，i (＝0, 1, ..., N－1) 番目の足場の高さは hi で与えられます．最初０番目の足場にカエルがいて，
 以下のいずれかの行動を繰り返して N－1 番目の足場を目指します．
足場 i から足場 i＋1 へと移動する (コストは | hi－hi＋1|) 　 足場 i から足場 i＋2 へと移動する (コストは | hi－hi＋2|) カエルが 
N－1 番目の足場にたどり着くまでに要するコストの総和の最小値を求めてください．

入力：7
      2 9 4 5 1 6 10
出力：最小コスト

絶対値メソッド abs()
"""
from typing import List


def frog(N: int, h: List[int]) -> int:
    dp = [2000000000]*N
    dp[0] = 0
    if N >= 2:
        dp[1] = abs(h[1]-h[0])
    for i in range(1, N):
        temp1 = dp[i-1]+abs(h[i]-h[i-1])
        temp2 = dp[i-2]+abs(h[i]-h[i-2])
        dp[i] = int(min(temp1, temp2))
        print(dp)
    return dp[N-1]


if __name__ == "__main__":
    N = int(input())
    h = list(map(int, input().split()))
    print(N, h)
    print(f'{frog(N, h)}')
