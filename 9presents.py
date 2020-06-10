n = int(input())
a = list(map(int,input().split()))
key = [0]*n
for i in range(0,len(a)):
    idx = a[i]-1
    val = i+1
    key[idx] = val
print(*key)