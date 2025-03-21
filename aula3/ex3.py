def calcular_notas(valor):
    cinquenta = valor // 50
    dez = (valor % 50) // 10
    um = (valor % 50) % 10
    return cinquenta, dez, um

valor = int(input("Digite o valor total: "))

n50, n10, n1 = calcular_notas(valor)
print(f"{n50} notas de 50, {n10} notas de 10, {n1} notas de 1")
