n,m=list(map(int,input().split()))
choice=['B','W']
for i in range(n):
    arr=list(input())
    for j in range(m):
        if arr[j]=='.':
            arr[j]=choice[(i+j)%2]
    print("".join(arr))