n,d=map(int,input().split())
arr=list(map(int,input().split()))
tot=tottime=0
for i in range(n):
    tot+=arr[i]
tottime=tot+(n-1)*10
if d<tottime:
    print(-1)
else:
    print((d-tot)//5)