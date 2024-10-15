tamanho_arquivo = float(input("Tamanho do arquivo (em MB): "))
velocidade = float(input("Velocidade em Mbps: "))
tempo_necessário = tamanho_arquivo / velocidade
minutos_necessarios = tempo_necessário // 60

print("Minutos necessários:", minutos_necessarios)