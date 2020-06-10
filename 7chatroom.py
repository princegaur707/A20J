s=input()
flag=0
for char in s:
    if char == 'h' and flag==0:
        flag+=1
    elif char == 'e' and flag==1:
        flag+=1
    elif char == 'l' and flag==2:
        flag+=1
    elif char == 'l' and flag==3:
        flag+=1
    elif char == 'o' and flag==4:
        flag+=1
if flag==5:
    print("YES")
else:
    print("NO")
        