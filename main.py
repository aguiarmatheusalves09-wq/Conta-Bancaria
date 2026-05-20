from conta import Conta

conta = Conta()

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
        conta.sacar_money(valor)
    
    elif opcao == "2":
        valor = float(input("Valor para depositar: "))
        conta.deposita_money(valor)

    elif opcao == "3":
        print(f"Saldo atual: R${conta.saldo:.2f}")

    elif opcao == "4":
        Meses = input("Quanto meses de rendimento vc deseja: ")
        print(f"Rendimento: R${conta.rendimento_do_money(meses)}")

    elif opcao == "5":
        break

    else:
        print("Opção Inválida!")