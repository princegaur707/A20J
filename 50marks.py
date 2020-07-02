n,m=map(int,input().split())
mat=[]
for i in range(n):
    row=list(input())
    row=[int(i) for i in row]
    mat.append(row)
topper=set()
mat=list(zip(*mat))
r,c=len(mat),len(mat[0])
for i in range(r):
    for j in range(c):
        print("i,j:",i,j)
        if mat[i][j] == max(mat[j]):
            topper.add(j+1)
        print(topper)
print(len(topper))