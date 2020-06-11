n = int(input())
a = list(map(int,input().split()))
key = [0]*n
for i in range(0,len(a)):
    idx = a[i]-1
    val = i+1
    key[idx] = val
print(*key)

n=int(input())
arr=list(map(int,input().split()))
list1=[arr.index(i)+1 for i in range(1,n+1)]
for i in list1:
    print(i,end=" ")