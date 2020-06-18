n,m = map(int,input().split())
ans = []
for i in range(n):
    a = list(map(int,input().split()))
    b = min(a[1:])
    if b < m:
        ans.append(i+1)
if ans:
    print(len(ans))
    print(*sorted(ans))
else:
    print(0)


#Another method
n,v=map(int,input().split())
mat=[]
arr=[]
for i in range(n):
    mat.append(list(map(int,input().split())))
for i in range(len(mat)):
    for j in range(1,mat[i][0]+1):
        if mat[i][j]<v:
            arr.append(i+1)
            break
print(len(arr))
for i in arr:
    print(i,end=" ")