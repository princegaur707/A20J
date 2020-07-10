n=int(input())
d={}
for i in range(n):
    team=input()
    try:
        d[team]=d[team]+1
    except:
        d[team]=1
print(max(d,key=lambda x: d[x]))