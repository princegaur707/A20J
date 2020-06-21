n=int(input())
mat=[]
for i in range(n):
    mat.append(list(map(str,input())))
a=mat[0][0];b=mat[0][1]
flag=False
if a==b:
    flag=True
for i in range(n):
    for j in range(n):
        if flag==False:
            if i==j or n-i-1==j:
                if mat[i][j]==a:
                    pass
                else:
                    flag=True
                    break
            else:
                if mat[i][j]==b:
                    pass
                else:
                    flag=True
                    break
if flag:
    print("NO")
else:
    print("YES")
            
    