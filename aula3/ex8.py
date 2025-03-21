import math

def graus_para_radianos(graus):
    return graus * (math.pi / 180)


graus = float(input("Digite o ângulo em graus: "))


radianos = graus_para_radianos(graus)
print(f"O ângulo em radianos é: {radianos:.4f}")
