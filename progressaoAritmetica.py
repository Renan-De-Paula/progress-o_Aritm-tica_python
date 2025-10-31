# Solicita o primeiro termo da progressão
primeiro = int(input("Primeiro Termo: "))

# Solicita a razão da progressão aritmética
razao = int(input("Razão: "))

# Solicita a quantidade de termos da progressão
progrecao = int(input("Quantidade de progressão: "))

# Inicializa o termo atual com o primeiro valor informado
termo = primeiro

# Contador começa em 1
cont = 1

# Laço para gerar e exibir os termos da progressão
while cont <= progrecao:
    print(f"{termo}", end=" - ")
    termo += razao  # Próximo termo da PA
    cont += 1       # Incrementa o contador

# Finaliza a exibição
print("FIM")