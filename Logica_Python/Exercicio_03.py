# 3. Escreva um algoritmo que o professor informa quantos alunos possui e calcule a média aritmética das 3 notas de cada alunos, 
# imprime se aprovou ou reprovou, apresenta média de cada aluno, apresente a média da turma inteira e a porcentagem de alunos aprovados e reprovados.
def quantidade_alunos():
    qtd = int(input("Informe a quantidade de alunos na sala: "))
    print(f"A quantidade de alunos é: {qtd}")
    return qtd
    
def notas_alunos(qtd_alunos):
    soma_medias_turma = 0
    alunos_aprovados = 0
    alunos_reprovados = 0
    
    for i in range(1, qtd_alunos + 1):
        nota1 = float(input(f"Qual a 1ª nota do {i}º aluno? "))
        nota2 = float(input(f"Qual a 2ª nota do {i}º aluno? "))
        nota3 = float(input(f"Qual a 3ª nota do {i}º aluno? "))
        
        media_aluno = (nota1 + nota2 + nota3) / 3
        soma_medias_turma += media_aluno
        print(f"A média do aluno {i} é: {media_aluno:.2f}")
                
        if media_aluno < 7:
            print("O aluno foi reprovado!\n")
            alunos_reprovados = alunos_reprovados + 1
        
        else:
            print("O aluno foi aprovado!\n")
            alunos_aprovados = alunos_aprovados + 1

    media_turma = soma_medias_turma / qtd_alunos
    porc_aprovados = (alunos_aprovados / qtd_alunos) * 100
    porc_reprovados = (alunos_reprovados / qtd_alunos) * 100    
    print("\nRESULTADO FINAL DA TURMA")
    print(f"Média geral da turma: {media_turma:.2f}")
    print(f"Alunos aprovados: {alunos_aprovados} ({porc_aprovados:.1f}%)")
    print(f"Alunos reprovados: {alunos_reprovados} ({porc_reprovados:.1f}%)")
        
qtd_alunos = quantidade_alunos()
notas_alunos(qtd_alunos)
