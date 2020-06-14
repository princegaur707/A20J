n,m,a,b=map(int,input().split())
print(min((n//m)*b+(n%m)*a,((n//m)+1)*b),n/a)