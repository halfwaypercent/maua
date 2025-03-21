import math

def radianos_para_graus(radianos):
    return radianos *  180 / math.pi


radianos = float(input("Digite o ângulo em radianos: "))


graus = radianos_para_graus(radianos)
print(f"O ângulo em graus é: {graus:.4f}")

