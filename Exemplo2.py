camisa = 0
options  = 0

while options != 4:
    print("Digite 1 para inserir no estoque: \n")
    print("Digite 2 para remover no estoque: \n")
    print("Digite 3 para consultar no estoque: \n")
    print("Digite 4 para SAIR \n")

    options = int(input("Escolha: \n"))

    if options == 1:

        qtd=int(input("Camisas para inserir\n"))
        camisa = camisa + qtd
        print("Total camisas = ", camisa, "\n")
        input("Digite <ENTER> para continuar\n") 

    elif options == 2:

        qtd=int(input("Camisas para retirar\n"))
        if qtd <= camisa:
            camisa = camisa - qtd
            print("Total camisas = ", camisa, "\n")
            input("Digite <ENTER> para continuar\n") 

        else:
            print("Quantidade insuficiente \n")
            input("Digite <ENTER> para continuar\n") 

    elif options == 3:
        print("Total camisas = ", camisa, "\n")
        input("Digite <ENTER> para continuar\n") 

    elif options == 4:
        print("TCHAU\n")
        break

    else:
        print("Opcão inválida \n")
        input("Digite <ENTER> para continuar\n") 




 

