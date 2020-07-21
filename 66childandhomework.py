mat=[]
for i in range(4):
    mat.append(input())
arr=sorted(mat,key=lambda x:len(x))
brr=sorted(mat,key=lambda x:len(x),reverse=True)
if (len(arr[-1])-2)>=(2*len(arr[0])-2):
    print(arr[0][0])
elif (len(brr[0])-2)>=(2*(len(brr[-1])-2)):
    print("Hello!")
    print(brr[0][0])
else:
    print('C') 