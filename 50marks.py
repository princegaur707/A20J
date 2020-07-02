n,m=map(int,input().split())
mat=[]
for i in range(n):
    arr=input()
    arr=[int(i) for i in arr]
    mat.append(arr)
mat=list(zip(*mat))
topper=set()
r,c=len(mat),len(mat[0])
for i in range(r):
    for j in range(c):
        if mat[i][j]==max(mat[i]):
            topper.add(j+1)
print(len(topper))