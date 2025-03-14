def c_para_F(c):
    return c * (9 / 5) + 32

c= float(input("Digite a temperatura em Celsius: "))
f = c_para_F(c)

print(f"A temperatura em Fahrenheit é: {f:.2f}")