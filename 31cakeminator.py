r,c=map(int,input().split())
mat=[]
for i in range(r):
    mat.append(list(str(input())))
row=set();col=set()
for i in range(r):
    for j in range(c):
        if mat[i][j]=="S":
            row.add(i)
            col.add(j)
print(r*c - len(row)*len(col))

