arr=[0,0]
arr[0],arr[1]=map(int,input().split())
def gcd(a,b):
    print(a,b)
    if b==0:
        return a
    else:
        return gcd(b,a%b)
c=-1
print(gcd(a,b))
for i in range(1,10**18+1):
    if gcd(i,b)==1 and gcd(i,a)!=1:
        arr.append(c)
        break
print(arr.sort())