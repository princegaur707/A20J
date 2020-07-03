n=int(input())
mat=[]
flag=False
for i in range(n):
    row=list(map(int,input().split()))
    mat.append(row)
for num in mat:
    if num[0]%2==0 and num[1]%2!=0:
        flag=True;break
    elif num[0]%2!=0 and num[1]%2==0:
        flag=True;break
mat=list(zip(*mat))
if sum(mat[0])%2==0 and sum(mat[1])%2==0:
    print(0)
elif sum(mat[0])%2==1 and sum(mat[1])%2==1 and flag==True:
    print(1)
else:
    print(-1)