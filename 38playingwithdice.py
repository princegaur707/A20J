a,b=map(int,input().split())
w=d=l=0
for i in range(1,7):
    if abs(i-a)<abs(i-b):
        w+=1
    elif abs(i-a)>abs(i-b):
        l+=1
    else:
        d+=1
print(w, d, l)