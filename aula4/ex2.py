def cosh(x):
    e = 2.718
    x = (e**x + e**(-x)) / 2

    return (x)

x=float(input("digite o numero para receber seu cosseno hiperbolico: "))
print("O cosseno hiperbolico de",x,"é",cosh(x))