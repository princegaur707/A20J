n = int(input())
x = list(map(int,input().split()))
p = x[0]
m = []
for i in range(1, n):
    for a, b in m[:-1]:
        if (a < p < b) ^ (a < x[i] < b):
            print("yes")
            exit()
    m.append([min(p,x[i]),max(p,x[i])])
    p = x[i]
    
print("no")
