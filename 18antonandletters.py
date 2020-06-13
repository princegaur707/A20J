arr=list(str(input()))
s=set()
for ch in arr:
    if ch.isalpha():
        s.add(ch)
print(len(s))