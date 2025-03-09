"""
    メモ化を行って高速化を狙う！！！
    めっちゃはええ！
"""

def fibo(n:int)->int:
    
    if n==0:
        return 0
    if n==1:
        return 1
    if memo.get(n):
        return memo[n]
    
    memo[n]=fibo(n-1)+fibo(n-2)
    return memo[n]

if __name__=='__main__':
    memo={}
    print(fibo(100))
    print(fibo(100))
    print(fibo(100))
    print(fibo(100))
    print(fibo(100))
    print(fibo(100))
    