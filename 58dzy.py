n=int(input())
res=[]
for i in range(n):
    res.append(list(map(int,input().split())))
res.sort(key= lambda x:(x[0],x[1]))
print(res)
flag=False
for i in range(1,len(res)):
    if res[i-1][0]<res[i][0] and res[i-1][1]>res[i][1]:
        flag=True
        break
if flag:
    print("Happy Alex")
else:
    
    print("Poor Alex")