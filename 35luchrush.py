n,k=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int,input().split())))#taking f,t
joy=-float("inf")
for i in arr:
    if i[1]<=k:
        tempjoy=i[0]
    else:
        tempjoy=i[0]-(i[1]-k)
    if tempjoy>joy:
        joy=tempjoy
print(joy)