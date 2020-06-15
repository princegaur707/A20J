x1,y1,x2,y2=map(int,input().split())
if x1==x2:
    len=abs(y2-y1)
    print(x1+len,y1,x2+len,y2)
elif y1==y2:
    len=abs(x2-x1)
    print(x1,y1+len,x2,y2+len)
elif abs(x2-x1)!=abs(y2-y1):
    print("-1")
else:
    print(x1,y2,x2,y1)
    