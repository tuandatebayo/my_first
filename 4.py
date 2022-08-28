import math
def cal(x, y):
 h=0
 if x <y -2:
    h=3*x**2-math.log(y)
 elif y-2 <= x <= y+2:
    h=(x+y)/2+8
 elif x > y +2:
    h=y**3+2*math.sin(x)
 return h
x=float(input())
y=float(input())
print(cal(x,y))
x1=[]
x2=[]
a=-2
b=5
while a<=6:
    x1.append(a)
    a+=0.5
while b>=-11:
    x2.append(b)
    b+=-1
for i in range (len(x1)):
    print(cal(x1[i],x2[i]))


