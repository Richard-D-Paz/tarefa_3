import random

matriz = [[]]
jogos = int(input("Quantos jogos serão gerados?: "))

while len(matriz) < jogos:
    numAleatorio = random.randint(1, 60)

    # Adiciona um número aleatório à linha atual da matriz
    if len(matriz[-1]) < 6:
        matriz[-1].append(numAleatorio)
    else:
        # Se a linha atual já tem 6 elementos, cria uma nova linha
        matriz.append([numAleatorio])

# Verifica se a última linha não tem 6 elementos e completa com números aleatórios
while len(matriz[-1]) < 6:
    numAleatorio = random.randint(1, 60)
    matriz[-1].append(numAleatorio)

# Se houver uma linha extra gerada ele exclui
if len(matriz) > jogos:
    matriz.pop()

# Exibe a matriz
print("\nAlgumas sujestões sobre o quais números colocar na MEGA-CENA: \n2")
for linha in matriz:
    print(linha, "\n")
