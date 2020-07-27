lever=input()
i=0
ind=lever.index('^')
arr,brr=[],[]
for i in range(ind):
    if lever[i].isdigit():
        arr.append(int(lever[i])*abs(i-ind))
for i in range(ind,len(lever)):
    if lever[i].isdigit():
        brr.append(int(lever[i])*abs(i-ind))
if sum(arr)>sum(brr):
    print("left")
elif sum(arr)<sum(brr):
    print("right")
else:
    print("balance")