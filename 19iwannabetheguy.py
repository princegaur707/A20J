n=int(input())
a=set(range(1,n+1))
x=list(map(int,input().split()))
y=list(map(int,input().split()))
x.pop(0)
y.pop(0)
if set(x+y)==a:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")