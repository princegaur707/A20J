n=int(input())
customers=list(map(int,input().split()))
mat=[]
for i in range(n):
    mat.append(list(map(int,input().split())))
min=float('inf')
for i in range(len(mat)):
    currenttot=sum(mat[i])*5+len(mat[i])*15
    if currenttot < min:
        min=currenttot
print(min)