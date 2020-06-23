n =  int(input())
a = []
for i in range(n):
    x,y = map(int,input().split())
    a.append((x,y))
sx = sorted(a,key=lambda t:t[0]*10000+t[1])
sy = sorted(a,key=lambda t:t[1]*10000+t[0])
ix = set()
iy = set()
for i in range(1,n-1):
    if sx[i][0] == sx[i-1][0] == sx[i+1][0]:
        ix.add(sx[i])
    if sy[i][1] == sy[i-1][1] == sy[i+1][1]:
        iy.add(sy[i])
print(len(ix&iy))