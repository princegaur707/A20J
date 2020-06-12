n=int(input())
arr=list(map(int,input().split()))
time=arr.index(max(arr))
mini=101
for i in range(n):
    if arr[i]<=mini:
        mini=arr[i]
        index=i
if index<time:
    print(time+n-index-2)
else:
    print(time+n-index-1)
        