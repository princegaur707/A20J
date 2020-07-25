import urllib.request, json
response = urllib.request.urlopen("https://mettl-arq.s3-ap-southeast-1.amazonaws.com/questions/iit-kanpur/cyber-security-hackathon/round1/problem1/defaulttestcase.txt")
string=response.read()
string=str(string)
print(string)
string=string[2:len(string)-3]
string.replace("\n","#")
print(string)
mat=string.split("#")
print(string)
d=dict()
for i in range(len(mat)):
    string=mat[i]
    string.replace(" ","")
    if string==string[::-1]:
        d[i+1]=len(string)
res = not d
if res:
    d[0]=0
print(d)