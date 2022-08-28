import math
def quadratic_equation(a, b, c):
    delta=b**2-4*a*c
    if a==0:
        return -c/b
    else:
        if delta > 0:
            x1=(-b+math.sqrt(delta))/(2*a)
            x2=(-b-math.sqrt(delta))/(2*a)
        elif delta == 0:
            x1=x2=-b/(2*a) 
        else:
            return 'No roots'
    return x1, x2
a=int(input())
b=int(input())
c=int(input())
print(quadratic_equation(a, b, c))

