import math
x1 = float(input('x1 '))
y1 = float(input('y1 '))
x2 = float(input('x2 '))
y2 = float(input('y2 '))
a = (x2 - x1)
a = a*a
b = y2 - y1
b = b*b
c = a + b
c = math.sqrt(c)
print('distancia ',c)