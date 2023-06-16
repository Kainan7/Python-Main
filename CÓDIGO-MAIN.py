1# Função para cadastrar um novo cliente
def cadastrar_cliente():
    print("=== Cadastro de Clientes ===")
    email = input("E-mail: ")

    # Verifica se o e-mail possui um formato válido
    if "@" not in email:
        print("E-mail não saiu corretamente, por favor tente novamente.")
        return

    contato = input("Contato: ")

    # Verifica se o contato possui apenas números e tem 11 dígitos
    if not contato.isdigit() or len(contato) != 11:
        print("Por favor, insira apenas números no número para contato (incluindo o DDD) com 11 dígitos.")
        return

    nome = input("Nome COMPLETO: ")

    # Verifica se o nome começa com letra maiúscula
    if not nome[0].isupper():
        print("A primeira letra do nome deve ser digitada em maiúsculo.")
        return

    # Adiciona o cliente ao arquivo "clientes.txt"
    with open("clientes.txt", "a") as arquivo:
        arquivo.write(f"{email};{contato};{nome}\n")

    print("Cliente cadastrado com sucesso!")

# Função para listar os clientes cadastrados
def listar_clientes():
    print("=== Lista de Clientes ===")
    with open("clientes.txt", "r") as arquivo:
        clientes = arquivo.readlines()
        for cliente in clientes:
            email, contato, nome = cliente.strip().split(";")
            print(f"E-mail: {email} | Contato: {contato} | Nome: {nome}")

# Função para remover um cliente
def remover_cliente():
    print("=== Remover Cliente ===")
    email_cliente = input("Digite o e-mail do cliente a ser removido: ")

    with open("clientes.txt", "r") as arquivo:
        clientes = arquivo.readlines()

    with open("clientes.txt", "w") as arquivo:
        removido = False
        for cliente in clientes:
            if email_cliente not in cliente:
                arquivo.write(cliente)
            else:
                removido = True

        if removido:
            print("Cliente removido com sucesso.")
        else:
            print("Cliente não encontrado.")

# Função para exibir o menu de produtos
def exibir_menu_produtos():
    print("=== Menu de Produtos ===")
    print("1. Jogos")
    print("2. Controles")
    print("3. Consoles")
    print("4. Acessórios para PC's")
    print("5. Sair")

# Função para exibir os produtos e preços
def exibir_produtos(produtos):
    print("=== Produtos Disponíveis ===")
    for i, produto in enumerate(produtos, start=1):
        nome = produto["nome"]
        preco = produto["preco"]
        print(f"{i}. {nome} --- R${preco}")

# Função para adicionar um item ao carrinho de compras
def adicionar_item_carrinho(carrinho, produtos):
    opcao_produto = input("Escolha um produto: ")

    try:
        index = int(opcao_produto) - 1
        produto = produtos[index]
        carrinho.append(produto)
        print(f"{produto['nome']} adicionado ao carrinho.")
    except (ValueError, IndexError):
        print("Opção inválida.")

# Função para exibir o carrinho de compras
def exibir_carrinho(carrinho):
    print("=== Carrinho de Compras ===")
    total = 0
    for produto in carrinho:
        nome = produto["nome"]
        preco = produto["preco"]
        total += preco
        print(f"{nome} --- R${preco}")
    print(f"Total: R${total}")

# Função para remover um item do carrinho de compras
def remover_item_carrinho(carrinho):
    exibir_carrinho(carrinho)
    opcao_produto = input("Escolha o número do produto a ser removido: ")

    try:
        index = int(opcao_produto) - 1
        produto = carrinho.pop(index)
        print(f"{produto['nome']} removido do carrinho.")
    except (ValueError, IndexError):
        print("Opção inválida.")

# Função para registrar os pedidos
def registrar_pedidos(carrinho):
    with open("pedidos.txt", "a") as arquivo:
        for produto in carrinho:
            nome = produto["nome"]
            preco = produto["preco"]
            arquivo.write(f"{nome};{preco}\n")

# Função para exibir o menu de pagamento
def exibir_menu_pagamento():
    print("=== Modo de Pagamento ===")
    print("1. Pix")
    print("2. Débito")
    print("3. Boleto")

# Função para finalizar a compra
def finalizar_compra():
    opcao_pagamento = input("Escolha uma opção de pagamento: ")

    if opcao_pagamento == "1":
        print("Pagamento realizado via Pix.")
    elif opcao_pagamento == "2":
        print("Pagamento realizado via Débito.")
    elif opcao_pagamento == "3":
        print("Pagamento realizado via Boleto.")
    else:
        print("Opção inválida.")

    opcao_finalizar = input("Deseja finalizar a compra? (Sim/Não): ")

    if opcao_finalizar.upper() == "SIM":
        print("Obrigado pela preferência! Volte sempre!")
    else:
        print("Compra não finalizada.")

# Função principal do programa
def main():
    # Lista de produtos
    jogos = [
        {"nome": "Battlefield", "preco": 100},
        {"nome": "Red Dead Redemption 2", "preco": 150},
        {"nome": "Need For Speed", "preco": 50},
        {"nome": "GTA", "preco": 90}
    ]

    controles = [
        {"nome": "Joystick para PC", "preco": 25},
        {"nome": "Controles para PS4", "preco": 150},
        {"nome": "Controles para Xbox", "preco": 150}
    ]

    consoles = [
        {"nome": "PlayStation 4", "preco": 2000},
        {"nome": "Xbox One", "preco": 1900},
        {"nome": "Nintendo", "preco": 2000}
    ]

    acessorios_pc = [
        {"nome": "Fonte para PC", "preco": 100},
        {"nome": "Memória RAM", "preco": 150},
        {"nome": "Processador", "preco": 500},
        {"nome": "Caixinha de som", "preco": 50},
        {"nome": "Monitor", "preco": 100}
    ]

    carrinho = []

    while True:
        print("=== Menu Principal ===")
        print("1. Cadastro de Clientes")
        print("2. Listar Clientes")
        print("3. Remover Cliente")
        print("4. Menu de Produtos")
        print("5. Registrar Pedidos")
        print("6. Modo de Pagamento")
        print("7. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_cliente()
        elif opcao == "2":
            listar_clientes()
        elif opcao == "3":
            remover_cliente()
        elif opcao == "4":
            exibir_menu_produtos()
            opcao_produto = input("Escolha uma opção: ")

            if opcao_produto == "1":
                exibir_produtos(jogos)
                adicionar_item_carrinho(carrinho, jogos)
            elif opcao_produto == "2":
                exibir_produtos(controles)
                adicionar_item_carrinho(carrinho, controles)
            elif opcao_produto == "3":
                exibir_produtos(consoles)
                adicionar_item_carrinho(carrinho, consoles)
            elif opcao_produto == "4":
                exibir_produtos(acessorios_pc)
                adicionar_item_carrinho(carrinho, acessorios_pc)
            elif opcao_produto == "5":
                break
            else:
                print("Opção inválida.")
        elif opcao == "5":
            exibir_carrinho(carrinho)
            opcao_carrinho = input("Escolha uma opção (1. Remover, 2. Voltar): ")

            if opcao_carrinho == "1":
                remover_item_carrinho(carrinho)
            elif opcao_carrinho == "2":
                continue
            else:
                print("Opção inválida.")
        elif opcao == "6":
            exibir_menu_pagamento()
            finalizar_compra()
        elif opcao == "7":
            break
        else:
            print("Opção inválida.")

    registrar_pedidos(carrinho)

if __name__ == "__main__":
    main()
