"""
    whileループにしてみた
    計算量：3-1同様
"""
if __name__=='__main__':
    a=list(map(int, input().split()))
    v = int(input())
    exist=False
    print(a)
    i=0
    while (i<len(a)):
        if a[i]==v:
            exist=True
            place=i
        i+=1
    if exist==True:
        print(f"Yes in {place}")
    else:
        print("No")