"""
    メモ化再帰
    
    入力：7
        2 9 4 5 1 6 10
    出力：最小コスト
"""
dp = []
h = []


def rec(i: int):
    if dp[i] < 200000:
        return dp[i]
    if i == 0:
        dp[0] = 0
        return 0
    result = 200000
    # 前のデータはちゃんと，recで呼び出そう
    result = int(min(result, rec(i-1)+abs(h[i]-h[i-1])))
    if i >= 2:
        result = int(min(result, rec(i-2)+abs(h[i]-h[i-2])))
    # メモ
    dp[i] = result
    return result


if __name__ == '__main__':
    N = int(input())
    dp = [200000]*N
    h = list(map(int, input().split()))
    print(rec(N-1))
