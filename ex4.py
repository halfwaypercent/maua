def calcular_area_trapezio(B, b, h):
    return ((B + b) * h) / 2

B = float(input("Digite a base maior: "))
b = float(input("Digite a base menor: "))
h = float(input("Digite a altura: "))

area = calcular_area_trapezio(B, b, h)
print(f"Área do trapézio: {area}")
