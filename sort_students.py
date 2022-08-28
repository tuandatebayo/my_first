def value(i):
    return (i[1], i[0])
def sort_students(l):
    a=sorted(l, key=value)
    
    return a
print(sort_students([('John', 9.75), ('Max', 9.5), ('James', 9.5), ('Henry', 8.5)]))

