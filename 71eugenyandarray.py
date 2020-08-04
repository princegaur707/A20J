n,m=map(int,input().split())
arr=list(map(int,input().split()))
mat=[]
for i in range(m):
    mat.append(list(map(int,input().split())))
l1=arr.count(1)
l2=arr.count(-1)
for i in mat:
    len=(i[1]-i[0])+1
    if len%2==0:
        if l1>=len//2 and l2>=len//2:
            print(1)
        else:
            print(0)
    else:
        print(0)