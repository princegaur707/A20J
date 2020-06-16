n,d=map(int,input().split())
arr=list(map(int,input().split()))
tot=sum(arr)
tottime=tot+(n-1)*10
if d<tottime:
    print(-1)
else:
    print((d-tot)//5)