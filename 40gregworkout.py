n = int(input())
a = list(map(int,input().split()))
from collections import defaultdict
d = defaultdict(list)
for i in range(0,len(a)):
    m = i%3
    d[m].append(a[i])
d = dict(d)
x = max(d.items(),key=lambda x:sum(x[1]))[0]
if x == 0:
    print("chest")
elif x == 1:
    print("biceps")
elif x == 2:
    print("back")


    
n=int(input())
mat=list(map(int,input().split()))
exe=['chest','biceps','back']
arr=[0,0,0]
i=0
while(n>0):
    n-=3
    try:
        arr[i%3]+=mat[i]
        arr[(i+1)%3]+=mat[i+1]
        arr[(i+2)%3]+=mat[i+2]
    except:
        break
    i+=3
ind=arr.index(max(arr))
print(exe[ind])

