n=int(input())
mat=[]
for i in range(n):
    mat.append(list(map(int,input().split())))
x=y=z=0
for num in mat:
    x+=num[0]
    y+=num[1]
    z+=num[2]
if x==0 and y==0 and z==0:
    print("YES")
else:
    print("NO")