"""
    最小値を求める問題
    時間計算量：O(N)
    空間計算量：O(N)
"""
if __name__=="__main__":
    N=list(map(int,input().split()))
    min_value=20000000
    for i in range(len(N)):
        if min_value>N[i]:
            min_value=N[i]
    print(f'min : {min_value}')
    