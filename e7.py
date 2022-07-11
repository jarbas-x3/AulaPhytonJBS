print("Reajuste salarial/n")
salario = float(input("Salario:"))
if (salario>1000):
    salnovo = salario+(salario*0.05)
elif (salario>500):
    salnovo = salario+(salario*0.10)
elif (salario>500):
    salnovo = salario+(salario*0.15)
print = ("Salario novo:", salnovo)
