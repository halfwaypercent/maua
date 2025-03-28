import math

def exibir_fracao(numerador, denominador):
    """
    Exibe a fração formatada com o numerador, denominador e uma barra alinhada.
    """
    largura = max(len(str(numerador)), len(str(denominador)))
    print(f"{numerador:>{largura}}")
    print("-" * largura)
    print(f"{denominador:>{largura}}")

def somar_fracoes(num1, den1, num2, den2):
    """
    Soma duas frações e retorna o numerador e denominador da fração resultante.
    """
    denominador_comum = den1 * den2
    numerador_resultante = (num1 * den2) + (num2 * den1)
    return numerador_resultante, denominador_comum

# Programa principal
if __name__ == "__main__":

    
    print("Digite os valores da primeira fração:")
    num1 = int(input("Numerador: "))
    den1 = int(input("Denominador: "))

    print("Digite os valores da segunda fração:")
    num2 = int(input("Numerador: "))
    den2 = int(input("Denominador: "))

    
    num_resultante, den_resultante = somar_fracoes(num1, den1, num2, den2)

    # Exibição do resultado
    print("\nResultado da soma das frações:")
    exibir_fracao(num_resultante, den_resultante)