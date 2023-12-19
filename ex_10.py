from datetime import date

pessoas = []
mulheres = []
idades_acima_media = []

# Variáveis para cálculo da média de idade
soma_idades = 0
total_pessoas = 0


while True:
    pessoa = {}
    
    pessoa['Nome'] = input("Digite o nome da pessoa: ")
    pessoa['Sexo'] = input("Digite o sexo biológico (Masculino/Feminino): ").capitalize()
    while pessoa['Sexo'] not in ['Masculino', 'Feminino']:
        pessoa['Sexo'] = input("Sexo biológico inválido. Digite novamente (Masculino/Feminino): ").capitalize()

    ano_nascimento = int(input("Digite o ano de nascimento da pessoa: "))
    hoje = date.today()
    pessoa['Idade'] = hoje.year - ano_nascimento


    pessoas.append(pessoa)
    
    # Atualiza variáveis para cálculo da média de idade
    soma_idades += pessoa['Idade']
    total_pessoas += 1
    
    # Verifica se é mulher e adiciona à lista de mulheres
    if pessoa['Sexo'] == 'Feminino':
        mulheres.append(pessoa['Nome'])
    
    continuar = input("Deseja continuar cadastrando? (Sim/Não): ").lower()
    if continuar != 'sim':
        break

# Verifica se há pessoas cadastradas
if total_pessoas > 0:
    media_idade = soma_idades / total_pessoas
    print(f"\nTotal de pessoas cadastradas: {total_pessoas}")
    print(f"Média de idade das pessoas: {media_idade:.2f}")

    # Verifica as idades acima da média
    for pessoa in pessoas:
        if pessoa['Idade'] > media_idade:
            idades_acima_media.append(pessoa['Idade'])


    print(f"\nMulheres cadastradas: {mulheres}")
    print(f"Idades acima da média: {idades_acima_media}")
else:
    print("Nenhuma pessoa cadastrada.")
