n=int(input())
mat=list(map(int,input().split()))
exe=['chest','biceps','back']
arr=[0,0,0]
for i in range(n):
    try:
        arr[i]+=mat[i]
        arr[i+1]+=mat[i+1]
        arr[i+2]+=mat[i+2]
    except:
        pass
print(arr)
ind=arr.index(max(arr))
print(exe[ind])