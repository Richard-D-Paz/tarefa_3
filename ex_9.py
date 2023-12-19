from datetime import date


ano_atual = date.today().year


nome = input("Digite o nome: ")
ano_nascimento = int(input("Digite o ano de nascimento: "))
ctps = int(input("Digite o número da carteira de trabalho (CTPS): "))


informacoes = {'Nome': nome, 'Ano de Nascimento': ano_nascimento, 'CTPS': ctps}

# Verifica se a CTPS é diferente de zero para obter informações profissionais
if ctps != 0:
    ano_contratacao = int(input("Digite o ano de contratação: "))
    salario = float(input("Digite o salário: "))
    informacoes['Ano de Contratação'] = ano_contratacao
    informacoes['Salário'] = salario

    # Calcula a idade do funcionário e anos restantes para aposentadoria
    idade = ano_atual - ano_nascimento
    informacoes['Idade'] = idade
    anos_contribuicao = ano_atual - ano_contratacao
    anos_restantes_aposentadoria = 35 - anos_contribuicao
    informacoes['Anos Restantes para Aposentadoria'] = anos_restantes_aposentadoria


print("\nInformações completas do funcionário:")
for chave, valor in informacoes.items():
    print(f"{chave}: {valor}")
