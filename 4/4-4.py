"""
    フィボナッチ数列
    計算回数:177回 N=10のとき
    計算 O(2^N) 
    これよりはだいぶ少ないな
    ↓ どうやって改善する?
    メモ化 動的計画法
"""



num=0
def fibo(n:int)->int:
    global num
    num+=1
    # print(f'{num}回目：フィボナッチが{n}で呼ばれました')
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo(n-1)+fibo(n-2)
 


if __name__=="__main__":
    print(fibo(100))
    print(fibo(100))
    print(fibo(100))
    print(fibo(100))
    print(fibo(100))