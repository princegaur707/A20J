n,m=map(int,input().split())
a=['B','W']
for i in range(n):
	s=list(input())
	for j in range(m):
		if s[j]=='.':
			s[j]=a[(i+j)%2]
	print(''.join(s))