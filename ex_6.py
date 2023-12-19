clientes = [
    {"nome": "Fulano", "idade": 25},
    {"nome": "Fulana", "idade": 17},
    {"nome": "Ciclano", "idade": 20},
    {"nome": "Beltrano", "idade": 18},
    {"nome": "Maria", "idade": 16}
]

# Variáveis para contar clientes maiores e menores de idade
clientes_maiores_idade = 0
clientes_menores_idade = 0



for cliente in clientes:
    nome = cliente["nome"]
    idade = cliente["idade"]

    # Verifica se o cliente é maior de idade ou menor de idade
    if idade >= 18:
        print(f"{nome} é maior de idade")
        clientes_maiores_idade += 1
    else:
        print(f"{nome} é menor de idade")
        clientes_menores_idade += 1



print(f"\nQuantidade de clientes maiores de idade: {clientes_maiores_idade}")
print(f"Quantidade de clientes menores de idade: {clientes_menores_idade}")
