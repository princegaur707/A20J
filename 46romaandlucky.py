def cnt(n,k):
    cnt = 0
    while n:
        if n%10 in (4,7):
            cnt+=1
        n = n//10
    return cnt <= k
n,k = map(int,input().split())
a = list(map(int,input().split()))
a = list(filter(lambda x:cnt(x,k),a))
print(len(a))