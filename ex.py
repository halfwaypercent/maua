from math import sqrt

def LerValores(N, X):
    for i in range(N):
        valor = float(input(f"Digite o valor {i+1}: "))
        X.append(valor)

def calcular_media(X):
    return sum(X) / len(X)

def calcular_desvio_padrao(X, media):
    soma = sum((x - media) ** 2 for x in X)
    return sqrt(soma / len(X))


N = int(input("Digite a quantidade de valores: "))
X = []
LerValores(N, X)
media = calcular_media(X)
desvio = calcular_desvio_padrao(X, media)
print(f"Média: {media:.2f}")
print(f"Desvio padrão: {desvio:.2f}")

