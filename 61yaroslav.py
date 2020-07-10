from collections import Counter
n=int(input())
arr=list(map(int,input().split()))
arr=Counter(arr)
b=[]
for i in arr:
    b.append(arr[i])
b.sort(reverse=True)
for i in range(1,len(b)):
    b[0]-=b[i]
if b[0]<2:
    print("YES")
else: 
    print("NO")
    