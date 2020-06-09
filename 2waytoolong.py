t=int(input())
while t:
    string=input()
    l=len(string)
    if l<11:
        print(string)
    else:
        print(string[0]+str(l-2)+string[-1])
    t-=1