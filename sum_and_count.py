def sum_and_count(inp):
    a=[]
    b=[]
    for i in inp:
        sum=0
        count=0
        if type(i) == int:
            sum+=i
            count+=1
        else:
         for k in i: 
            sum+=int(k)
            count+=1
        a.append(sum)
        b.append(count)
    return a, b
inp = ((1,2,5), (3,7,5,10), (1))

sum_list, cnt_list = sum_and_count(inp)
print(*sum_list)
print(*cnt_list)