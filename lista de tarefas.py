def quebra_linha():
    print("-" * 30)

lista_de_tarefas = {}

while True:
    quebra_linha()
    print("1 - Adicionar nova tarefa")
    print("2 - Listar tarefas")
    print("3 - Sair")
    quebra_linha()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        tarefa = input("Adicione sua tarefa: ").lower()
        if tarefa in lista_de_tarefas:
            lista_de_tarefas[tarefa] += 1
        else:
            lista_de_tarefas[tarefa] = 1    
    elif escolha == "2":
        for tarefa, quantidade in lista_de_tarefas.items():
            print(tarefa, "-", quantidade)
    elif escolha == "3":
        break
quebra_linha()
