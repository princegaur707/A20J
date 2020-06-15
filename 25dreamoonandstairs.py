n,m=map(int,input().split())
tot=n//2+n%2
flag=True
while tot<=n:
    if tot%m==0:
        flag=False
        break
    else:
        tot+=1
if flag:
    print("-1")
else:
    print(tot)