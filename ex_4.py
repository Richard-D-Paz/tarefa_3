numeros = []
pares = []
impares = []

while True:
        entrada = input("Digite um número (ou 'sair' para terminar): ")

       
        if entrada.lower() == 'sair':
            break

        try:
            num = int(entrada)  # Tenta converter para número inteiro

            # Adiciona o número à lista principal
            numeros.append(num)

            # Verifica se o número é par ou ímpar e adiciona à lista correspondente
            if num % 2 == 0:
                pares.append(num)
            else:
                impares.append(num)

        except ValueError:
            print("Por favor, insira um número inteiro válido.")

    # Exibe o conteúdo das três listas geradas
print("\nLista completa de números inseridos:")
print(numeros)
print("\nLista de números pares:")
print(pares)
print("\nLista de números ímpares:")
print(impares)





"""
lista = []
impar = []
par = []

while True:
        num = input("Digite um valor numérico (ou 'sair' para terminar): ")

        # Verifica se o usuário deseja sair do programa
        if num.lower() == 'sair':
            break

        try:
            num = int(num)  # Tenta converter para número

            if num % 2 == 0:
                 num.append(par)
            else:
                 num.append(impar)
                 
        except ValueError:
            print("Por favor, insira um num numérico válido.")
"""      