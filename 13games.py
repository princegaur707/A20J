n=int(input())
mat=[]
for i in range(n):
    mat.append(list(map(int,input().split())))
cnt=0
for x in range(len(mat)):
    for y in range(len(mat)):
        if x!=y:
            if mat[x][0]==mat[y][1]:
                cnt+=1
print(cnt)
            