saldo = 400
NumeroDeSaquesPorDia = 3
extrato = []
while True:
    print (""" 
    #######################
    #   MENU PRINCIPAL    #
    #######################
    # (1) Deposito        #
    # (2) Saque           #
    # (3) Extrato         #
    # (0) Encerrar ope    #
    """)
    # Ler a opcao do usuario
   
    opcao = input("Bom dia! \nO que deseja fazer: ")
    print(" ")

    if ( opcao == "1" ):
        valorDepositado = float( input("\nInsira o valor a depositar: R$") )
        while(valorDepositado <= 0):
            print("Valor invalido!\nTente novamente.")
            valorDepositado = float(input("Insira o valor a depositar: R$"))
        saldo += valorDepositado
        print("Operação conclluida com sucesso!")
        extrato.append([ "DEPOSITO:  >>", valorDepositado])

    elif ( opcao == "2" ):
        if ( NumeroDeSaquesPorDia > 0 ):
            
            while(True) :
                valor_do_saque = float(input("\nInsira o valor a ser sacado: R$"))
                if(saldo < valor_do_saque):
                    print("Saldo insuficiente!")

                elif(valor_do_saque > 500):
                    print("Nao pode sacar mais de R$500,00 por vez.")

                else:
                    NumeroDeSaquesPorDia -= 1
                    print("saque de {} realizado com sucesso" .format(valor_do_saque))
                    saldo -= valor_do_saque
                    extrato.append(["SAQUE:  <<", valor_do_saque])
                    break
                
        else:
            print("Voce atingiu o limite diario de saques.\nAguarde até amanhã para tentar outro saque.")

    else:
        comprimento_maximo = 10
        if(opcao =="3"):
            print("""
            ########################
            ##  EXTRATO BANCARIO  ##
            ########################
            """)
            for operacao,valor in extrato:
                print("# {:<15} {:>{}}".format(operacao, valor, comprimento_maximo))

            print("""###########################
            SALDP ATUAL: {:.2f}""" .format(saldo))  
            
        elif (opcao == "0"):
            print("Finalizando sistema...\nAté logo!")
            break
        else:
            print("Opção inválida!\nTente novamente.")
               
    