x=eval(input("qual é o cateto oposto?"))
y=eval(input("qual é o cateto adjacente?"))

import math 
c=math.sqrt(x**2+y**2)

z=y/c

print(c,z)
