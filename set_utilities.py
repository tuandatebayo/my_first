

def  process(filepath):
    file= open(filepath)
    data  = file.read()
    line = data.split()
    c={}
    for i in range (len(line)):
        if i%3 ==0:
            line[i]+=':'
            m = {}
            c[line[i]] = m
    for i in range (len(line)):
        if line[i-1] in c and line[i] not in c[line[i-1]]:
            c[line[i-1]][line[i]]= int(line[i+1])
        elif line[i-1] in c and line[i] in c[line[i-1]]:
            c[line[i-1]][line[i]]+=int(line[i+1])
    for i in c:
        print(i)
        c[i] = sorted(c[i].items())
        for m in c[i]:
            print(m[0],m[1])
