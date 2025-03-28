import math


def alcance(velocidade, angulo):
    g = 9.8  #aceleração da gravidade

    angulo = math.radians(angulo)

    alcance = (velocidade ** 2/ g) * (math.sin(2 * angulo)) 
    """calcula o alcance de um projétil lançado com uma velocidade inicial e um angulo de lançamento"""
    return alcance

velocidade = float(input("Digite a velocidade inicial (em m/s): "))
angulo = float(input("Digite o angulo (em graus): "))

print("O alcance é de %.2f metros" % alcance(velocidade, angulo))