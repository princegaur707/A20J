n,k=map(int,input().split())
arr=list(map(int,input().split()))
cnt=0
for i in arr:
    if i+k<=5:
        cnt+=1
print(cnt//3)