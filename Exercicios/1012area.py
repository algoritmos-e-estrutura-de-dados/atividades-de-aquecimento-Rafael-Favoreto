a = float(input())
b = float(input())
c = float(input())
pi = 3.14159
def triangulo_retangulo():
    area = (a*c)/2
    return area
def raio_circulo():
    raio = c/(2*pi)
    return raio
def area_trapezio():
    area = ((a + b)*c)/2
    return area
def area_quadrado():
    area = b*b
    return area
def area_retangulo():
    area = a*b
    return area
print('triangulo:',triangulo_retangulo(), '\ncirculo:',raio_circulo() ,'\ntrapezio:',area_trapezio(), '\nquadrado:',area_quadrado(), '\nretangulo',area_retangulo())