n = int(input())
res = str()
for i in range(n):
    res+=str(input())
print(res)
if res == res[::-1]:
    print("YES")
else:
    print("NO")