def bissexto(ano):
    """
    Verifica se um ano é bissexto.

    Returns:
        bool: True se o ano for bissexto, False caso contrário.
    """
    # Um ano é bissexto se não terminar em 00 e for divisível por 4
    if ano % 100 != 0 and ano % 4 == 0:
        return True
    else:
        # Um ano é bissexto se terminar em 00 e for divisível por 400
        if ano % 100 == 0 and ano % 400 == 0:
            return True
        else:
            # Caso contrário, não é bissexto
              return False

def main():
    try:
        ano = int(input("Digite um ano para verificar se é bissexto: "))
        if bissexto(ano):
            print(f"O ano {ano} é bissexto.")
        else:
            print(f"O ano {ano} não é bissexto.")
    except ValueError:
        print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()