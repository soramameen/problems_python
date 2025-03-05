"""
    計算量：O(N)
    空間計算量：O(N)
"""



if __name__=='__main__':
    a=list(map(int, input().split()))
    v = int(input())
    exist=False
    print(a)
    for i in range(len(a)):
        if a[i]==v:
            exist=True
    if exist==True:
        print("Yes")
    else:
        print("No")