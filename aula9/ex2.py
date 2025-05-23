n = int(input("Digite a quantidade de números: "))
quadrados = 0
contador = 0

while contador < n:
    valor = float(input("Digite um número: "))
    quadrados += valor ** 2
    print( quadrados)
    contador += 1

print("A soma dos quadrados dos números é: ", quadrados)