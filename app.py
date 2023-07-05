def cadastrar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    
    with open("contatos.txt", "a") as arquivo:
        arquivo.write(f"{nome},{telefone}\n")
    
    print("Contato cadastrado com sucesso!")

def consultar_telefone():
    nome = input("Digite o nome do contato para consultar o telefone: ")
    
    with open("contatos.txt", "r") as arquivo:
        for linha in arquivo:
            contato = linha.strip().split(",")
            if contato[0] == nome:
                print(f"Telefone do contato '{nome}': {contato[1]}")
                return
    
    print(f"O contato '{nome}' não foi encontrado.")

def excluir_contato():
    nome = input("Digite o nome do contato que deseja excluir: ")

    with open("contatos.txt", "r") as arquivo:
        contatos = arquivo.readlines()

    with open("contatos.txt", "w") as arquivo:
        for linha in contatos:
            contato = linha.strip().split(",")
            if contato[0] != nome:
                arquivo.write(linha)

    print(f"O contato '{nome}' foi excluído com sucesso.")

def exibir_menu():
    print("Menu de opções:")
    print("1. Cadastrar contato")
    print("2. Consultar telefone")
    print("3. Excluir contato")
    print("4. Sair")

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_contato()
    elif opcao == "2":
        consultar_telefone()
    elif opcao == "3":
        excluir_contato()
    elif opcao == "4":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
