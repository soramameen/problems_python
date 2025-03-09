"""
    ユークリッドの互除法をrecursiveで解く
    a= b*c +d
    b= d*e +f
    みたいなやつ
    最後に商が0の時の余りが最大公約数みたいな
"""
def GCD(m:int,n:int):
    if n == 0 :
        return m
    l = m % n
    print(f"{m}={n}*a+{l}")
    return GCD(n,l)

    
    
if __name__=="__main__":
    print(GCD(51,15))