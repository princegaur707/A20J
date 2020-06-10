mat = []
for i in range(0,5):
    mat.append(list(map(int,input().split())))
for i in range(0,5):
    for j in range(0,5):
        if mat[i][j] == 1:
            idx1 = abs(i+1-3)
            idx2 = abs(j+1-3)
            print(idx1+idx2)
            break