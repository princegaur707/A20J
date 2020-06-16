n,m=map(int,input().split())
row1="#"+"."*(m-1)
row2="."*(m-1)+"#"
row=row2
for i in range(1,n+1):
    if i%2==1:
        print("#"*m)
    else:
        print(row)
        if row==row1:
            row=row2
        else:
            row=row1
            