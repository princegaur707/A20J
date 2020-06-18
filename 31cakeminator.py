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

r,c=map(int,input().split())
arr=[];row=[];col=[]
total=tot=0
for i in range(r):
    arr.append(input())
for i in range(r):
    for j in range(c):
        if arr[i][j]=='S':
            row.append(i)
            col.append(j)
for i in range(r):
    if i not in row:
        tot+=c
for j in range(c):
    if j not in col:
        total+=r-(tot)//c
print(total+tot)