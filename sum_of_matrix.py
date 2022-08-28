temp = input().split(' ')
m, n = int(temp[0]), int(temp[1])

a = []
b = []
for i in range(m):
  a.append(input().split(' '))
for i in range(m):
  b.append(input().split(' '))
c = []
for i in range(m):
    for k in range(n):
        c.append(int(a[i][k])+int(b[i][k]))
for i in range (m):
    for k in range (n):
        print(c[k+3*i], end=' ')
    print()


