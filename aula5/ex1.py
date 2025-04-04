def formatar_tempo(horas, minutos, segundos):
    
    
    print(f"{horas:02d}h{minutos:02d}m{segundos:02d}s")

# Programa principal
if __name__ == "__main__":
    
    horas = int(input("Digite a quantidade de horas: "))
    minutos = int(input("Digite a quantidade de minutos: "))
    segundos = int(input("Digite a quantidade de segundos: "))

   
    formatar_tempo(horas, minutos, segundos)