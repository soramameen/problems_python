def recursive(n:int)->int:
    if n==0:
        return 0
    return n + recursive(n-1)

if __name__=='__main__':
    print(recursive(5))