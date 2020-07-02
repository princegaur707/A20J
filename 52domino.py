n=int(input())
mat=[]
for i in range(n):
    row=list(map(int,input().split()))
    mat.append(row)
mat=list(zip(*mat))
if sum(mat[0])%2==0 and sum(mat[1])%2==0:
    print(0)
elif sum(mat[0])%2==1 and sum(mat[1])%2==1 and mat[0]!=mat[1]:
    print(1)
else:
    print(-1)