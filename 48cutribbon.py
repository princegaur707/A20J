import math
n,a,b,c=map(int,input().split())
dp = [0]*(n+1)
for i in range(1,n+1):
    if i-a<0:
        x = -math.inf
    else:
        x = dp[i-a]
    if i-b<0:
        y = -math.inf
    else:
        y = dp[i-b]
    if i-c<0:
        z = -math.inf
    else:
        z = dp[i-c]
    dp[i] = max(x+1,y+1,z+1)
    print(dp)    
print(dp[-1])