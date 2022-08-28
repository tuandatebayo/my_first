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

list(a).sort()
a.sort(reverse = True, key = lambda wordtup: wordtup[1])
for i in  a:
    print(a[0])

