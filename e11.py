print("calcular imc. Peso/alt*alt/n")
for cont in range(1,5):
    peso=float(input('Peso:'))
    altura=float(input('Altura:'))
    imc=peso/(altura*altura)
    if (imc>40):
        print('Obesidade 3')
    elif (imc>=35):
        print('Obesidade 2')
    elif (imc>=30):
        print('Obesidade 1')
    elif(imc>=25):
        print('Sobrepeso')
    elif(imc>=18.5):
        print('Peso normal')
    elif(imc<18.5):
        print('abaixo do peso')