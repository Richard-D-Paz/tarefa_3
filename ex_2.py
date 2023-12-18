contagem1 = []

contagem2 = []

print("\n", "por favor, digite 'sim' ou 'nao' ", "\n")

pergunta1 = input("Você telefonou para a vítima?: ")

pergunta2 = input("Esteve no local do crime?: ")

pergunta3 = input("Mora perto da vítima?: ")

pergunta4 = input("Devia para vítima?: ")

pergunta5 = input("Já trabalhou com a vitima?: ")


#//////////////////////////////// 1
if pergunta1 == "sim" :
    contagem1.append(1)

else:
    contagem2.append(1)
#//////////////////////////////// 2
if pergunta2 == "sim" :
    contagem1.append(1)

else:
    contagem2.append(1)
#//////////////////////////////// 3
if pergunta3 == "sim" :
    contagem1.append(1)

else:
    contagem2.append(1)
#//////////////////////////////// 4
if pergunta4 == "sim" :
    contagem1.append(1)

else:
    contagem2.append(1)
#//////////////////////////////// 5
if pergunta5 == "sim" :
    contagem1.append(1)

else:
    contagem2.append(1)
#//////////////////////////////// soma

contagem1Soma = sum(contagem1)
contagem2Soma = sum(contagem2)

#//////////////////////////////// texto lógico

if contagem1Soma == 2:
    print("Suspeito...")

elif contagem1Soma == 3 or contagem1Soma == 4:
    print("Cumplice")

elif contagem1Soma == 5:
    print("Assassino")

else:
    print("Inocente")

print(contagem1Soma)
print(contagem2Soma)