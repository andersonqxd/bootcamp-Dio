
import textwrap

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tR$ {valor:.2f}\n"
        print("\n === Deposito realizado com sucesso! ===")
        
    else:
        print("\n@@@ Valor de depósito deve ser maior que zero. @@@")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_de_saques, limite_de_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_de_saques > limite_de_saques
    
    if excedeu_saldo: 
        print("\n@@@ Operação falhou! Você não tem saldo sufuciente! @@@")
    
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque execedeu o limite! @@@")
    
    elif excedeu_saques:
        print("\n@@@ Operação Falhou Número maximo de saques excedidos! @@@")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: \t\tR$ {valor:.2f}\n"
        print("\n=== Saque realizado com sucesso! ===")
    
    else:
        print("\n@@@ Operação falhou, Valor informado é invalido! @@@")
    
    return saldo, extrato

def exibir_Extrato(saldo,/,*extrato):
    print("\n================== EXTRATO ==================")
    print("Não foram realizados movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$: {saldo:.2f}")
    print("\n=============================================")
    
def criar_Usuario(usuarios):
    cpf = input("Informe seu cpf (somente numeros!): ")
    usuario = filtar_Usuario(cpf, usuarios)
    
    if usuario:
        print("\n@@@ Já existe usuario com esse CPF! @@@")
        return
    nome = input("Digite seu nome completo: ")
    data_nascimento = input("Informe a sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (Logadouro - nro -bairro - cidade/sigla da cidade): ")
    
    usuarios.append( {
        "nome":nome,
        "data_nascimento":data_nascimento,
        "cpf":cpf,
        "endereco":endereco
    } )
    
def filtar_Usuario(cpf,usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios 
                          if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_Conta(agencia,numero_conta, usuarios):
    cpf = input("Informe o CPF do ususario: ")
    usuario = filtar_Usuario(cpf, usuarios)
    
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return{"agencia": agencia, "numero_conta":numero_conta, "usuario":usuario}
    
    print("\n@@@ Usuario não encontrado, fluxo de criação de conta encerrada! @@@")

def lista_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            c/c:\t\t{conta['numero_conta']}
            Titular:\t{conta["usuario"]["nome"]}
        """    
        print("=" * 100)
        print(textwrap.dedent(linha))    

def menu():
    menu = """\n
    ================= menu =================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tLista Contas
    [nu]\tNovo Usuario
    [q]\tSair
    =>"""
    return input(textwrap.dedent(menu))


def main():
    limite_de_saques = 3
    agencia = "0001"
    
    saldo = 0
    extrato = ""
    limite = 500
    numero_de_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        
        match opcao:
            case "d":
                valor = float( input("informe o valor de deposisto: ") )
                
                saldo, extrato = depositar(saldo, valor, extrato)
            case "s":
                valor = float( input("Informe um valor de saque: ") )
                
                saldo, extrato = sacar (
                    saldo = saldo,
                    valor = valor,
                    extrato = extrato,
                    limite = limite,
                    numero_de_saque = numero_de_saques,
                    limite_de_saques = limite_de_saques,
                    
                )
            case "e":
                exibir_Extrato(saldo,extrato=extrato)
            case "nu":
                criar_Usuario(usuarios)
            case "nc":
                numero_contas = len(contas) + 1
                conta = criar_Conta(agencia,numero_contas, usuarios)
                
                if conta:
                    contas.append(conta)
                    numero_contas += 1
            case "lc":
                lista_contas(contas)    
            case "q":
                print("Operação finalizada!")
                break
            case _:
                print("Opção Inválida")
        
main()
