a, b, c = input().split()

a = float(a)
b = float (b)
c = float(c)
pi = 3.14159

area_triangulo = (a * c) / 2
area_triangulo = "{:.3f}".format(area_triangulo)
raio_circulo = pi * c**2
raio_circulo = "{:.3f}".format(raio_circulo)
area_trapezio = ((a + b) * c) / 2
area_trapezio = "{:.3f}".format(area_trapezio)
area_quadrado = b**2
area_quadrado = "{:.3f}".format(area_quadrado)
area_retangulo = a * b
area_retangulo = "{:.3f}".format(area_retangulo)

print("TRIANGULO:", area_triangulo)
print("CIRCULO:", raio_circulo)
print("TRAPEZIO:", area_trapezio)
print("QUADRADO:", area_quadrado)
print("RETANGULO:", area_retangulo)