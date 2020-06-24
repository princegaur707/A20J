def cnt(n,k):
    cnt = 0
    while n:
        if n%10 in (4,7):
            cnt+=1
        n = n//10
    return cnt <= k