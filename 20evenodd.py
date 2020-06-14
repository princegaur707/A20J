n,k=map(int,input().split())
half=n-n//2
if k<=half:
    print(2*k-1)
else:
    k=k-half
    print(k*2)