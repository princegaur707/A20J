def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
def power(a,b):
    for i in range(b):
        if a**i==b:
            return i
k=int(input())
l=int(input())
if gcd(k,l)==k:
    print("YES")
    print(power(k,l)-1)
else:
    print("NO")