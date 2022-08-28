import numpy as np
a=np.arange(0, 9).reshape(3, 3)
print(np.sum(a, axis=1,keepdims=True))
x=np.sum(a, axis=1,keepdims=True)
print(a/x)