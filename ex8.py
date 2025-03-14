import math

def graus_para_radianos(graus):
    return graus * (math.pi / 180)

# Entrada do ângulo em graus
graus = float(input("Digite o ângulo em graus: "))

# Cálculo e saída
radianos = graus_para_radianos(graus)
print(f"O ângulo em radianos é: {radianos:.4f}")
