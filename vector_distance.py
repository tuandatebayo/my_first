import math

def vector_distance(v1, v2, **kwargs):
    def manhattan(v1,v2):
        l=0
        for i in range (len(v1)):
            l+=abs(v1[i]-v2[i])
        return l
    def euclidean(v1, v2):
        a=0
        for i in range (len(v1)):
            a+=(v1[i]-v2[i])**2
        l=math.sqrt(a)
        return float("{:.1f}".format(l))
    def lenght(v):
        a=0
        for i in v:
            a+=i**2
        return math.sqrt(a)
    def cosine(v1,v2):
        a=0
        b=1
        for i in range (len(v1)):
            a+=v1[i]*v2[i]
        b=lenght(v1)*lenght(v2)
        return float("{:.9f}".format(a/b))
    if kwargs['norm'] == 'manhattan':
        return manhattan(v1,v2)    
    elif kwargs['norm'] == 'cosine':
        return cosine(v1,v2)
    else:
        return euclidean(v1, v2)
#vẫn bị sai test ẩn


print(vector_distance([1, 2,3], [4, 6,8], norm='manhattan'))

            
            
        


