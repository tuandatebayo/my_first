import math
def exp(n):
    res=0
    a=0
    while abs(res-math.e**n)>= 1e-9:
        res+=(n**a)/math.factorial(a)
        a+=1
    return res
def sin(n):
    while n >= 2 * math.pi:
        n -= 2 * math.pi
    res=0
    a=0
    while abs(res-math.sin(n))>=1e-9:
        res+=(-1)**a*n**(2*a+1)/math.factorial(2*a+1)
        a+=1
    return res
def cos(n):
    while n >= 2 * math.pi:
        n -= 2 * math.pi
    res=0
    a=0
    while abs(res-math.cos(n))>=1e-9:
        res+=(-1)**a*n**(2*a)/math.factorial(2*a)
        a+=1
    return res


