#crie dois vetores com o nome e notas de 4 alunos
#mostre o nome e a nota dos alunos acima da media da turma
nomes =["ana", "pedro", "João", "Samara"]
notas = [9,10,7,5]

#media da turma
soma = 0
for nota in notas:
    soma += nota
media = soma/len(notas)
print('Média da turma:', media)
for i in range(len(notas)):
    if notas[i]> media:
        print('Aluno com nota acima da média: ', nomes[i],
        'Nota: ', notas[i] )