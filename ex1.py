frase = input("Digite uma frase: ")
palavra = input("Digite a palavra a ser buscada: ")

contador = 0
for i in range(len(frase) - len(palavra) + 1):
    if frase[i:i+len(palavra)] == palavra:
        contador += 1

print(f'A palavra "{palavra}" aparece {contador} vez(es) na frase.')