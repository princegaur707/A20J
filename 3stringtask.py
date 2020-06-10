s = str(input())
s = s.lower()
import re
s = re.findall('[^aoyeui]',s)
print("." + ".".join(s))

s=input().lower()
vowel=['a','e','i','o','u','y']
