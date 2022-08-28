text = []
while True:
    try:
        text.append(input().split())
    except:
        break
a={}
for i in text:
    for k in i:
        if k not in a:
            a[k]=0
            print(a[k], end=' ')
        else:
            a[k]+=1
            print(a[k], end= ' ')
