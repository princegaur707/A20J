n,k = map(int,input().split())
cur , res = 0,0
for i in range(n):
    l,r = map(int,input().split())
    res += (r-l+1) + (l-cur-1)%k
    cur = r
    print("r-l-1,l-cur-1,(l-cur-1)%k,res:",r-l-1,l-cur-1,(l-cur-1)%k,res)
print(res)