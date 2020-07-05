arr=list(map(int,input().split()))
c=((arr[1]*arr[2])/arr[0])**0.5
b=arr[1]/c
a=arr[0]/b
print(int(4*(a+b+c)))