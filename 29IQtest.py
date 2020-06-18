n=int(input())
arr=list(map(int,input().split()))
o=e=0
for i in arr:
    if i%2:
        o+=1
        if o>1:
            break
    else:
        e+=1
        if e>1:
            break
if e>1:
    for i in range(n):
        if arr[i]%2!=0:
            print(i+1)
            break
else:
    for i in range(n):
        if arr[i]%2==0:
            print(i+1)
            break
  