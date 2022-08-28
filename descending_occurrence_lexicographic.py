text = []
while True:
    try:
        text.append(input().split())
    except:
        break
a={}
for i in text:
    for k in i:
        if k in a:
            a[k]+=1
        else:
            a[k]=1
lst=[(i, a[i]) for i in a]
lst.sort()
lst.sort(reverse = True, key = lambda wordtup: wordtup[1])
for i in lst:
    print(i[0])