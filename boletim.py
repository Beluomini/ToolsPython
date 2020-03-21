#Retorna alunos aprovados de um vetor (media 7)--------------
def alunosAprovados(alunos,notas):
    passaram=[]
    for i in range(len (notas)):
        if (float(notas[i])>=7):
            passaram.append(alunos[i])
    return passaram

#Registra aluno/nota e vef se ele passou---------------------
def registroBoletim():
    qtdAlunos=int(input("Digite a quantidade de alunos: "))
    alunos=[]
    notas=[]
    nota=0
    for i in range(qtdAlunos):
        alunos.append(input("Digite o nome do aluno: "))
        nota=float(input("Digite sua nota: "))
        notas.append(nota)
    
    print("Dos alunos",alunos,"com as respectivas notas",notas,"passaram apenas: ",alunosAprovados(alunos,notas))
