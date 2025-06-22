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

    if opcao == 1:
        valor = float(input("Digite o valor a ser depositado: "))

        if valor > 0:
            saldo =+ valor
            extrato += f"Depósito de R$ {valor:.2f} reais \n"
        
        else: 
            print("Operação falhou! O valor informado é inválido, digite um valor maior que Zero")
            
    elif opcao == "q":
        break



