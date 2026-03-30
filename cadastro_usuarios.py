lista_usuarios = {}

while True:
    opcao = input("O que você deseja fazer? (adicionar, listar, excluir ou sair): ").lower()

    if opcao == "adicionar":
        nome = input("Adicione o nome do usuário: ")
        email = input("Adicione o email: ")
        idade = int(input("Adicione sua idade: "))

        if nome in lista_usuarios:
            print("Usuário já existe!")
        else:
            lista_usuarios[nome] = {
                "email": email,
                "idade": idade
            }

    elif opcao == "listar":
        for nome, dados in lista_usuarios.items():
            print(nome, "-", dados["email"], "-", dados["idade"])

    elif opcao == "excluir":
        if lista_usuarios:
            removido = lista_usuarios.popitem()
            print(f"Usuário removido: {removido[0]}")
        else:
            print("Lista vazia.")

    elif opcao == "sair":
        break

    else:
        print("Opção inválida.")