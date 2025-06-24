menu = """
digite o número de uma das opções abaixo 

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

print(menu)
extratos = ""


extratos += "deposito de 500 reais \n"
extratos += "saque de 500 reais \n"

while True:
    
    opcao = input(menu)
    print(opcao)

    if opcao == "1":
        valor = float(input("Digite o valor a ser depositado: "))

        if valor > 0:
            saldo =+ valor
            extrato += f"Depósito de R$ {valor:.2f} reais \n"
        
        else: 
            print("Operação falhou! O valor informado é inválido, digite um valor maior que Zero")

    
    elif opcao == "2":
        valor = float(input("Digite o valor a ser sacado: "))

        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        
        elif valor > limite:
            print("Operação falhou! O valor do saque excede o limite.")
        
        elif numero_saques >= LIMITE_SAQUES:
            print("Operação falhou! Você já realizou o número máximo de saques.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque de R$ {valor:.2f} reais \n"
            numero_saques += 1
        
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        break

    else:
      print("digite uma opção válida")
