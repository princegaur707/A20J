n,x=map(int,input().split())
mat=[]
for i in range(n):
    mat.append(list(map(int,input().split())))
current=0;i=time=0
while(i<n):
    if current+x<mat[i][0]:
        current+=x
    else:
        time+=mat[i][1]-current
        current+=time
        i+=1
print(time)

n,k = map(int,input().split())
cur , res = 0,0
for i in range(n):
    l,r = map(int,input().split())
    res += (r-l+1) + (l-cur-1)%k
    cur = r
print(res)