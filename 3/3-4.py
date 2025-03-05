"""
    和が最小になるペアを探す
"""
if __name__=="__main__":
    N =int(input())
    K= int(input())
    a= list(map(int,input().split()))
    b= list(map(int,input().split()))
    min_value=2000000
    for i in range(len(a)):
        for j in range(len(b)):
            sum=a[i]+b[j]
            if sum <min_value and sum>=K:
                min_value=sum
    print(min_value)