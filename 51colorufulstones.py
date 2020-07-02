s=input()
t=input()
l1,l2=len(s),len(t)
i,j,count=0,0,1
while i<l1 and j<l2:
    if s[i]==t[j]:
        i+=1
        j+=1
        count+=1
    else:
        j+=1
print(count)