n=int(input())
arr=list(map(int,input().split()))
from collections import defaultdict
d=defaultdict(list)
for i in range(len(arr)):
    d[arr[i]].append(i)
print(d.items())
mn=min(len(d[1]),len(d[2]),len(d[3]))
if mn==0:
    print(mn)
else:
    print(mn)
    for i in range(mn):
        print(d[1][i]+1,d[2][i]+1,d[3][i]+1)
    
    