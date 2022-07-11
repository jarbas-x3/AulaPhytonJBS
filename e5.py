print("Verificar se os números são pares ou ímares \n")
rep=3
for cont in range(rep):
    numero = int(input('Número: '))
    if (numero%2) == 0:
       print("Par")
    else:
       print("Ímpar")