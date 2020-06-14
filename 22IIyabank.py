def convert(n):
    s=[]
    s.extend(n)
    return (s)
def a(x):
    x.pop()
    return(int("".join(x)))
def b(x):
    x.pop(-2)
    return(int("".join(x)))
n=input()
if int(n)>=0:
    print(n)
else:
    w=convert(n)
    w.pop(0)
    v=convert(n)
    v.pop(0)
    print(max(-a(w),-b(v)))
    