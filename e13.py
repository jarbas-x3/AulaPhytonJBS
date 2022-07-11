num = []
#inicia n com 1 para entrar no loop
n = 1

while n:
    n = int(input("Digite n: "))
    # só adiciona na lista se for diferente de zero
    if n!=0 : num.append(n)
print(num)
# para inverter uma lista, é só usar [:;-]
print(num[n])