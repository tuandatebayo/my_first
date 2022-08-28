import string
a=list(string.ascii_lowercase)
n=int(input())
str=list(input())
for i in str:
    if i == ' ':
        print(' ', end='')    
    else:
        s=a.index(i)
        z=s+n%26
        if s+n%26 > 25:
            z=s+n%26-26
        print(a[z],end='')