import math

def calcular_area_heron(a, b, c):
    s = (a + b + c) / 2  # Semiperímetro
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Fórmula de Herão
    return area

# Entrada dos lados do triângulo
a = float(input("Digite o lado a do triângulo: "))
b = float(input("Digite o lado b do triângulo: "))
c = float(input("Digite o lado c do triângulo: "))

# Cálculo e saída
area = calcular_area_heron(a, b, c)
print(f"A área do triângulo é: {area:.2f}")
