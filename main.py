def main():
    import boletim
    import quantidadeProteinaAlimentacao
    import toolsString
    print("--------MENU--------")
    print("0 ----------- Sair")
    print("1 ----------- Boletim")
    print("2 ----------- Proteina")
    print("3 ----------- Encontrar consoantes em String")
    opcao = int(input("Digite uma opção: "))
    if(opcao == 0):
        exit
    elif(opcao == 1):
        boletim.registroBoletim()
    elif(opcao == 2):
        quantidadeProteinaAlimentacao.main()
    elif(opcao == 3):
        toolsString.consoantes()


