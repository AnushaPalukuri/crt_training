a,b=0,1
l=[a,b]
while len(l)<26:
    s=a+b
    l.append(s)
    a=b
    b=s
print(l)
