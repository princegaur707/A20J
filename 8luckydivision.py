#best but only for range 1-1000
n = int(input())
if n%4 == 0 or n%7 == 0 or n%44 == 0 or n%77 == 0 or n%477 == 0 or n%744 == 0 or n%444 == 0 or n%777 == 0 or n%474 == 0 or n%747 == 0 or n%47 == 0 or n%74 == 0:
    print("YES")
else:
    print("NO")

#will work on any range
n=input()
import re
from itertools import combinations,chain
s=re.findall('[^47]',n)
if s:
    l=len(n)
    n=int(n)
    cnt=0
    arr=[]
    series=list(chain.from_iterable(combinations(['4','7'],r) for r in range(1,l+1)))
    for s in series:
        arr.append("".join(s))
    for i in arr:
        if n%int(i)==0:
            print("YES")
            cnt=1
            break
    if cnt==0:
        print("NO")
else:
    print("YES")
