from conta import Conta

conta = Conta(100)

while True:
    print("\ Menu ")
    print("1 - Sacar")
    print("2 - Depositar")
    print("3 - Ver Saldo")
    print("4 - Calcular Rendimento")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        valor = float(input("Valor para sacar: "))
        conta.sacar(valor)