n =  int(input())
a = []
for i in range(n):
    x,y = map(int,input().split())
    a.append((x,y))
sx = sorted(a,key=lambda t:t[0]*10000+t[1])
sy = sorted(a,key=lambda t:t[1]*10000+t[0])
ix = set()
iy = set()