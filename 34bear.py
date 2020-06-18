n,c=map(int,input().split())
arr=list(map(int,input().split()))
max=0
for i in range(1,len(arr)):
    if arr[i-1]-arr[i]>max:
        max=arr[i-1]-arr[i]
print(max-c) if max-c>0 else print(0)