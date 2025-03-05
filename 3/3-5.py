"""
    与えられた整数から何個かの整数を選んで 
    総和を W にできるかを調べる問題
    
    難しいところ
    - 全てのパターンの組み合わせを考える必要がある
    - 再帰関数を使えばできそうだがこの章では用いない
    
    アプローチ
    -2進数変換して0のとき選ばれてない，1のとき選ばれているとして
    全探索を行う
"""
if __name__=='__main__':
    a=list(map(int,input().split()))
    w=int(input())
    flag=False
    for i in range(2**len(a)):
        sum=0
        bin_i =bin(i)
        bin_i_num=(bin_i[2:].zfill(len(a)))
        for j in range(len(a)):
            if bin_i_num[j]=='1':
                sum+=a[j]
        if sum==w:
            flag=True
    if flag==True:
        print("success")
    else:
        print("no...")
            


