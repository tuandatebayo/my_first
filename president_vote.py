text = []
while True:
    try:
        text.append(input().split(' '))
    except:
        break
a=[]
b=[]
c=[]
for i in text:
    if i[0] not in a:
        a.append(i[0])
for i in a:
    d=0
    for n in text:
        if n[0]==i:
            d+=int(n[1])
    b.append(d)
for i in range (len(a)):
    c.append([a[i],b[i]])
c.sort()
for i in c:
    print(i[0], i[1])


    

