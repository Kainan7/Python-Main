import csv

#Função para cadastrar um cliente
def cadastrar_cliente():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")   
    #Abrir o arquivo "clientes.csv" em modo de escrita
    with open("clientes.csv", "a", newline="") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([nome, email, telefone])
    
    print("Cliente cadastrado com sucesso!")

#Função para exibir o menu de produtos
def exibir_menu():
    print("--- MENU ---")
    print("1. Jogo")
    print("2. Controle")
    print("3. Console")
    print("4. PC")
    print("5. Acessório")
    print("6. Sair")

#Função para registrar um pedido
def registrar_pedido():
    pedido = []
    total = 0
    
    while True:
        exibir_menu()
        opcao = input("Digite o número do produto desejado (ou 6 para sair): ")
        
        if opcao == "1":
            produto = "Jogo"
            preco = 50
        elif opcao == "2":
            produto = "Controle"
            preco = 100
        elif opcao == "3":
            produto = "Console"
            preco = 500
        elif opcao == "4":
            produto = "PC"
            preco = 1500
        elif opcao == "5":
            produto = "Acessório"
            preco = 30
        elif opcao == "6":
            break
        else:
            print("Opção inválida. Tente novamente.")
            continue
        
        plataforma = input("Digite a plataforma desejada (PC, Xbox, PlayStation, Nintendo): ")
        versao = input("Digite a versão do jogo (Digital ou Físico): ")
        
        pedido.append({"Produto": produto, "Plataforma": plataforma, "Versão": versao, "Preço": preco})
        total += preco
    
    print("Pedido registrado:")
    for item in pedido:
        print(item)
    
    print("Total da compra: R$", total)
    forma_pagamento = input("Digite a forma de pagamento: ")
    print("Obrigado por comprar conosco, volte sempre!")

#Função principal que exibe o menu principal
def main():
    while True:
        print("--- MENU PRINCIPAL ---")
        print("1. Cadastrar cliente")
        print("2. Registrar pedido")
        print("3. Sair") 
        opcao = input("Digite o número da opção desejada: ")
        
        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            registrar_pedido()
        elif opcao == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

#Execução do programa
main()