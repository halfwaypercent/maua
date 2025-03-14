import math

def calcular_area_heron(a, b, c):
    s = (a + b + c) / 2  # fase1
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # Fórmula de Herão
    return area


a = float(input("Digite o lado a do triângulo: "))
b = float(input("Digite o lado b do triângulo: "))
c = float(input("Digite o lado c do triângulo: "))


area = calcular_area_heron(a, b, c)
print(f"A área do triângulo é: {area:.2f}")
