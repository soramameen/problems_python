"""
   再帰関数の挙動確認
"""
def recursive(n:int)->int:
    print(f"再帰関数が {n} で呼び出されました")
    if n==0: # ベースケースと呼ぶ
        return 0
    result= n + recursive(n-1)
    print(result)
    return result

if __name__=='__main__':
    print(recursive(5))