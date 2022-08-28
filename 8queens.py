c = int(input())
s=[]
for i in range (c):
    s1=[]
    for j in range (8):
        s1.append(input().split(" "))
    s.append(s1)
for i in range(c):
    check =0
    for j in range(8):
        for k in range ((j+1),8):
            if int(s[i][j][1])==int(s[i][k][1]) or abs(int(s[i][j][1])-int(s[i][k][1])) ==abs(int(s[i][j][0])-int(s[i][k][0])) or int(s[i][j][0])==int(s[i][k][0]):
                check +=1
    if check ==0:
        print('NO')   
    else:
        print('YES')