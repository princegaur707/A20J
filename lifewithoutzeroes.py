I=lambda x:int(str(x).replace('0',''))
a=int(input())
b=int(input())
print("YNEOS"[I(a)+I(b)!=I(a+b)::2])