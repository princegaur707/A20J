from collections import Counter
k=int(input())
string=""
string+=input();string+=input();string+=input();string+=input()
string=list(string)
string=[i for i in string if i!='.']
string=Counter(string)
count=string.most_common(1)
try:
    cnt=count[0][1]
    if cnt<=2*k:
        print("YES")
    else:
        print("NO")
except:
    print("YES")