# Escreva um algoritmo que o professor informa quantos alunos possui e calcule a média aritmética das 3 notas 
# de cada alunos, imprime se aprovou ou reprovou, apresenta média de cada aluno, apresente a média da turma 
# inteira e a porcentagem de alunos aprovados e reprovados.

alunos = int(input("Digite quantos alunos você possui:"))
aprovados = 0
reprovados = 0
alunos_e_notas = []
soma_turma = 0

for i in range (1, alunos+1):
    nota1 = int(input(f"nota 1 do aluno {i}: "))
    nota2 = int(input(f"nota 2 do aluno {i}: "))
    nota3 = int(input(f"nota 3 do aluno {i}: "))
    media = nota1 + nota2 + nota3 
    media = media / 3

    if media >= 7:
        ar = ("Aprovado!")
        aprovados += 1
    else: 
        ar = ("Reprovado!")
        reprovados += 1

    alunos_e_notas.append(f"Aluno {i}, nota: {media:.2f}, {ar}\n")
    soma_turma += media

media_turma = soma_turma / alunos
porcentagem_aprovados = aprovados * 100 / alunos
porcentagem_reprovados = 100 - porcentagem_aprovados

print("------------------------------------------------------")
for i in range (0, alunos): print(alunos_e_notas[i])
print("------------------------------------------------------")
print(f"Media da turma: {media_turma:.2f}")
print("------------------------------------------------------")
print(f"porcentagem de alunos aprovados: {porcentagem_aprovados:.0f}%")
print(f"porcentagem de alunos reprovados: {porcentagem_reprovados:.0f}%")
