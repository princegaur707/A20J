y,k,n=map(int,input().split())
x=0
for i in range((y//k)*k+k,n+1,k):
    x=i-y
    print(x,end=" ")
if x==0:
    print(-1)
    