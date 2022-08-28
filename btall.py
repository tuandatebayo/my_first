def sum_of_digit(n):
    a=len(str(n))
    if a==1:
        return n
    else:
        return sum_of_digit(n//(10**(a-1)))+sum_of_digit(n%(10**(a-1)))

def dec_to_bin(n): 
  if (n // 2) == 0: 
    return str(n % 2) 
  else: 
    return dec_to_bin(n // 2) + str(n % 2)


def is_prime(n):
    if n == 2:
        return True
    else:
       for i in range(2, n):
           if n%i==0:
               return False
    return True

gcd = lambda a, b: b if a%b==0 else gcd(b,a%b)


def binary(n, lastDigit=1):
    if n == 0:
        return 0
    if n == 1:
        return 1 if (lastDigit == 0) else 2
    if lastDigit == 1:
        return binary(n - 1, 0) + binary(n - 1, 1)
    else:
        return binary(n - 1, 1)


def square_sum(n):
    if n==0 or n ==1:
        return n
    else:
        return n**2+square_sum(n-1)


power = lambda x, y: 1 if y == 0 else x if y == 1 else x*power(x, y - 1)


mid = lambda x, y, z: x if y<=x<=z or z<=x<=y else mid(z, x, y)


remove_duplicate
n = int(input())
arr = list(map(int, input().split()))
a = int(input())
arr = arr[:7]
clone = arr[:]
clone = list(map(lambda x : abs(x - a), clone))
min = min(clone)
for i in range (len(clone)):
    if clone[i]  == min:
        print(arr[i])

    