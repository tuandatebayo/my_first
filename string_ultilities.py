class string_utilities:
    def is_valid_parenthese(seft, a):        
        def check(a, b):
         if a=='{' and b == '}' or a== '[' and b == ']' or a =='(' and b==')':
            return True       
        d=list(a)
        b=len(d)
        if b%2!=0:
            return False
        else:
         while len(d)>0:
          for i in range(1,len(d)):           
            if check(d[i-1],d[i]) == True:
                    del d[i-1:i+1]
                    if len(d)==0:
                        return True
                    break
            if i==len(d)-1:
                return False
    def reverse_words(seft, a):
        b=a.split()
        for i in b[::-1]:
            print(i, end=' ')
        return ''
print(string_utilities().is_valid_parenthese('{[(])]}'))
print(string_utilities().is_valid_parenthese('{[()(({}))]}'))
print(string_utilities().reverse_words('Bach khoa Ha Noi'))