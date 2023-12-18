valores = []
valores_unicos = set()

while True:
        valor = input("Digite um valor numérico (ou 'sair' para terminar): ")

        if valor.lower() == 'sair':
            break

        try:
            valor = float(valor)  # Tenta converter para número

            # Verifica se o valor já foi inserido
            if valor not in valores_unicos:
                valores_unicos.add(valor)
                valores.append(valor)
            else:
                print("Este valor já foi adicionado anteriormente. Por favor, insira outro valor.")

        except ValueError:
            print("Por favor, insira um valor numérico válido.")

    # Ordena os valores únicos em ordem crescente
valores_unicos_ordenados = sorted(valores_unicos)


print("\nValores únicos digitados em ordem crescente:")
for valor in valores_unicos_ordenados:
        print(valor)
