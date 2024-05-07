def menu():
    menu = '''

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [nu] Criar Usuário
    [nc] Nova Conta
    [lc] Listar Conta
    [lu] Listar Usuários
    [q] Sair

    '''
    return input(menu)

def depositar(saldo, valor_deposito, extrato, /):
    if valor_deposito <= 0:
        print("favor, informar um valor superior a 0")
    else:
        saldo = saldo + valor_deposito
        extrato += f"Depósito: R${valor_deposito:.2f}\n"
        print(f"Seu saldo atual é de R${saldo}")

    return saldo, extrato
            
def sacar(*, saldo, valor_saque, extrato, limite, numero_saques, limite_saques):
    
    if valor_saque > saldo:
        print("Você não tem saldo o suficiente para efetuar o saque")
    
    elif valor_saque > limite:
        print(f"Você só tem R${limite} de limite para sacar. Favor, informar um valor inferior")
    
    elif numero_saques > limite_saques:
        print("Você já excedeu a quantidade de saques permitidas no dia!")

    elif valor_saque <= 0:
        print(f"Favor, informar valor superior a 0")
        
    elif valor_saque > 0:
        #numero_saques += 1
        saldo -= valor_saque
        extrato += f"Saque: R${valor_saque:.2f}\n"
        print(f"Saque efetuado com sucesso, você tem R${saldo} restantes na conta. Você também efetuou {numero_saques} saques de 3.")
    
    else:
        print("Operação falhou! Verifique suas entradas e tente novamente")
    
    return saldo, extrato

def extrato_final(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = int(input("Informe o CPF (somente número): "))
    
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Este usuário já existe")
            return #usuario[0] if usuario else None
        
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")
            
def criar_conta(agencia, numero_conta, usuarios):
    cpf = int(input("Informe o CPF (somente número): "))

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Conta criada com sucesso!")
            return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        else:
            print("Usuário não encontrado! Cadastre-se e tente novamente")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)

def listar_usuarios(usuarios):
    for usuario in usuarios:
        linha = f"""
            Nome: {usuario['nome']}
            Data de Nascimento: {usuario['data_nascimento']}
            CPF: {usuario['cpf']}
            Endereço: {usuario['endereco']}
        """
        print("="*100)
        print(linha)

def main():
    saldo = 0
    limite = 500.00
    LIMITE_SAQUES = 3
    numero_saques = 0
    extrato = ""
    usuarios = []
    AGENCIA = "0001"
    contas = []
    numero_conta = 1



    while True:

        opcao = menu()

        if opcao == 'd':
            valor_deposito = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor_deposito, extrato)

        elif opcao == 's':
            valor_saque = float(input("Favor, informar o quanto você quer sacar: "))

            numero_saques +=1 if valor_saque > 0 else 0 

            saldo, extrato = sacar(
                saldo = saldo,
                valor_saque = valor_saque,
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
            )

        elif opcao == 'e':
            extrato_final(saldo, extrato = extrato)
        
        elif opcao == 'nu':
            criar_usuario(usuarios)
        
        elif opcao == 'nc':
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta is not None:
                numero_conta += 1
                contas.append(conta)

        elif opcao == 'lc':
            listar_contas(contas)
        
        elif opcao == 'lu':
            listar_usuarios(usuarios)
        
        elif opcao == 'q':
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()