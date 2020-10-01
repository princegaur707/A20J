def count(coins,m,n):
    table=[[0 for i in range(n+1)] for j in range(m)]
    for i in range(m):
        table[i][0]=1
    for  i in range(1,n+1):
        if i%coins[0]==0:
            table[0][i]=1
        else:
            table[0][i]=0    
    for i in range(len(coins)):
        for j in range(1,n+1):
            if coins[i]>j:
                table[i][j]=table[i-1][j]
            else:
                table[i][j]=table[i-1][j]+table[i][j-coins[i]]    
    print (table[-1][-1])


count([2],1,3)