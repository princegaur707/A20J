n=int(input())
def printfunc(n):
    if n<5:
        print("O-|",end="")
    else:
        print("-O|",end="")
    print((n%5)*'O',end="")
    print("-",end="")
    print((4-(n%5))*'O')
if n==0:
    print("O-|-OOOO")
while (n):
    printfunc(n%10)
    n//=10