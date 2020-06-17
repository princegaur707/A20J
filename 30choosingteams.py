def solve(a,k):
    cnt = 0
    for i in range(0,len(a)):
        if 5 - a[i] >= k:
            cnt+=1
    return cnt//3

n,k = map(int,input().split())
a = list(map(int,input().split()))
print(solve(a,k))