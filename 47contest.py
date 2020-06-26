def calc(p,t):
    x = (3*p) / 10
    y = ((p) - ((p*t)/(250)))
    return max(x,y)

a,b,c,d = map(int,input().split())
p,q = calc(a,c),calc(b,d)
print(p,q)
if p > q:
    print("Misha")
elif p == q:
    print("Tie")
else:
    print("Vasya")