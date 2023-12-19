
alunos = {}

quantidade_alunos = int(input("Quantos alunos deseja registrar? "))

for i in range(quantidade_alunos):
    nome = input(f"Informe o nome do aluno {i+1}: ")
    media = float(input(f"Informe a média do aluno {i+1}: "))

    # Determina a situação do aluno com base na média
    if media >= 7:
        situacao = "Aprovado"
    elif 5 <= media < 7:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"

    # Adiciona as informações do aluno ao dicionário
    alunos[nome] = {"Média": media, "Situação": situacao}

# Exibe o conteúdo do dicionário na tela
print("\nInformações dos alunos:")
for nome, info in alunos.items():
    print(f"Nome: {nome} - Média: {info['Média']} - Situação: {info['Situação']}")
