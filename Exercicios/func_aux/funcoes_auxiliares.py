import random
from random import randint
from math import *

print(randint(5,10))
print(factorial(3))

random_number_0_1 = random.random()
#linha abaixo print numero random compreendido entre 0 e 1 (decimal)
print(random_number_0_1)
#linha abaixo print numero random compreendido entre 0 e 100 (inteiro)->(int)
print(int(random_number_0_1 * 100))

print("---------------------------")
print(abs(-2))
print(type(2.2))
print(max(1, 9 , -3, 20))
print(min("bca", "cde", "pt"))