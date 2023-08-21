# модули - его файлы
# встроенные модули
import colorama
print(colorama.Back.BLACK)
print(colorama.Fore.BLUE)
import math

p = math.pi
print(p)

from math import e as E

print(E)
# собвственные модули

from lesson4 import B

c = B('a', 'c')
c.c()
# 3 внешние модули
import colorama
print(colorama.Back.BLACK)