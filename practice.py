import urllib.request, json
response = urllib.request.urlopen(input1)
string=response.read()
string=str(string)
string=string[2:len(string)-3]
string.replace("\n","#")
string=string.split("#")
d=dict()
for i in range(len(mat)):
    string=matrix[i]
    string.replace(" ","")
    if string=string[::-1]:
        d[i+1]=len(string)


import re
regex = re.compile(
        r'^(?:https|ftp)s?://' 
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
        r'localhost|' 
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

if re.match(regex, "input1") is not None and string[-1:-4]==".txt":
    arr="file ok"
else:
    arr="file is not a text file"

#checking dictionary is empty or not
res = not d
if res:
    d[0]=0

