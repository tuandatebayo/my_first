def dictionary_convert(s):
    a=list(s)
    b=[]
    d=[]
    for i in a:
        if i not in b:
            c=a.count(i)
            b.append(i)
            d.append((i,c))
    return dict(d)
print(dictionary_convert('edcbaabcd'))

