s,n=map(int,input().split())
dragons=[]
for i in range(n):
    x,y=map(int,input().split())
    dragons.append((x,y))
dragons.sort(key=lambda x:(x[0],-x[1]))
flag=1
for i in dragons:
    if s>i[0]:
        s+=i[1]
    else:
        flag=0
        break
if flag:
    print("YES")
else:
    print("NO")
    