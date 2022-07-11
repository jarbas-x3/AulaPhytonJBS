print('Mostra n de 5 a 100 divisíveis de 7, mas não , múltiplos de 5')
for num in range(5, 100):
    if (num % 7 == 0) and (num % 5 != 0):
        print(num)