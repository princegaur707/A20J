n=int(input())
res=""
for i in range(n):
    res+=input()
print(res)
if res==res[::-1]:
    print("YES")
else:
    print("NO")
    