#Retorna as consoantes de uma string-------------------------
def consoantes():
    vetor=[]
    for i in range(10):
        a=input("Digite um caracter: ")
        vetor.append(a)
    vetorf=achar(vetor)
    print("Existem", len (vetorf),"consoantes, são elas:",vetorf)
