
pedidos = []
while True:
    print("\nMenu:")
    print("(C)adastrar novo pedido")
    print("(E)ntregar bebida")
    print("(S)air do programa")
    opcao = input("Escolha uma opção: ").strip().upper()

    if opcao == "C":
        nome = input("Digite o nome do cliente: ").strip()
        pedidos.append(nome)
        print(f"Pedido cadastrado para {nome}.")
    elif opcao == "E":
        if pedidos:
                nome = pedidos.pop(0)
                print(f"PEDIDO PRONTO: {nome.upper()}")
        else:
                print("Nenhum pedido pendente.")
    elif opcao == "S":
            print("Encerrando o programa.")
            break
    else:
            print("Opção inválida.")

