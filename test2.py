n=int(input())
lst1=input().split()
lst=[]
for i in lst1[0:n]:
    lst.append(int(i))
res=[lst[0]]
def check(n, k):
    if abs(n) < abs(k) and n*k < 0:
        return True
    return False

for i in range(1, len(lst)):
    a=len(res)
    b=[]
    for k in range (i,len(lst)):
        if check(res[a-1],lst[k]) == True:
            b.append(lst[k])
        if len(b)>0:
            if check(res[a-1],lst[k]) == False:
                break
    if len(b)>0:               
     if b[0] < 0:
        res.append(max(b))
     if b[0] > 0:
        res.append(min(b))
print(len(res))
