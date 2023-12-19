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


    if produto not in estoque:
        print("Produto não encontrado no estoque.")
    else:
        quantidade = int(input(f"Digite a quantidade de {produto} vendida: "))


        if quantidade > estoque[produto]:
            print("Quantidade solicitada não disponível no estoque.")
        else:


            estoque[produto] -= quantidade
            print(f"Venda realizada: {quantidade} unidades de {produto} foram vendidas.")


print("\nEstoque final após as vendas:")
print(estoque)
