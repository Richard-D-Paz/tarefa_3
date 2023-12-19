estoque = {
    'arroz': 50,
    'feijao': 30,
    'macarrao': 40,
    'leite': 60,
    'cafe': 20
}

# Simulação de vendas
while True:
    print("\nEstoque atual:", estoque)
    produto = input("Digite o produto vendido (ou 'sair' para encerrar): ").lower()

    if produto == 'sair':
        break

    # Verifica se o produto está disponível no estoque
    if produto not in estoque:
        print("Produto não encontrado no estoque.")
    else:
        quantidade = int(input(f"Digite a quantidade de {produto} vendida: "))

        # Verifica se a quantidade solicitada está disponível no estoque
        if quantidade > estoque[produto]:
            print("Quantidade solicitada não disponível no estoque.")
        else:
            
            # Realiza a baixa no estoque
            estoque[produto] -= quantidade
            print(f"Venda realizada: {quantidade} unidades de {produto} foram vendidas.")

# Exibe o estoque final após as vendas
print("\nEstoque final após as vendas:")
print(estoque)
