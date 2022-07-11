print ("Número positivo, negativo, neutro/n")
for num in range(1,4):
    num = int(input('Número:'))
    if (num>0):
        print(num,' Positivo')
    elif (num<0):
        print(num,' Negativo')
    elif (num==0):
        print(num,' Neutro')
