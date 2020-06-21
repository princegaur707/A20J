n=int(input())
mat=[]
for i in range(n):
    mat.append(list(map(str,input())))
#print(mat)
a=mat[0][0]
b=mat[0][1]
flag=False
for i in range(n):
    for j in range(n):
        if i==j and mat[i][j]==a:
            pass
        else:
            print("Here")
            flag=True
            break
        if i!=j and mat[i][j]==b:
            pass
        else:
            print("It is")
            flag=True
            break
if flag:
    print("NO")
else:
    print("YES")
            
    