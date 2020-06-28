a,b,c,d=map(int,input().split())
M=max(3*(a/10),a-(a/250)*c)
V=max(3*(b/10),b-(b/250)*d)
if M>V:
    print("Misha")
elif M<V:
    print("Vasya")
else:
    print("Tie")