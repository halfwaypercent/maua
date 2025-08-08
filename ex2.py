def ler_valores(n):
    valores = []
    for i in range(n):
        valor = float(input(f"Digite o valor {i+1}: "))
        valores.append(valor)
    return valores

n = int(input("Digite a quantidade de valores: "))
valores = ler_valores(n)
opcao = input("Exibir em ordem crescente (C) ou decrescente (D)? ").strip().upper()
if opcao == "C":
    valores.sort()
    print("Valores em ordem crescente:", valores)
elif opcao == "D":
    valores.sort(reverse=True)
    print("Valores em ordem decrescente:", valores)
else:
    print("Opção inválida.")