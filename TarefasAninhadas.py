lista = []

while True:
    tarefa = int(input("1 - Adicionar tarefa(s)\n2 - Visualizar tarefa(s)\n3 - Remover tarefa(s)\n4 - Encerrar\n"))

    if tarefa == 1:
        while True:
            nova_tarefa = input("Qual(is) tarefa(s) você deseja adicionar?\nSelecione 6 para voltar ao menu anterior.\n")
            if nova_tarefa == '6':
                break
            lista.append(nova_tarefa)
    elif tarefa == 2:
        if not lista:
            print("Não há tarefas para exibir.")
        else:
            for i, item in enumerate(lista):
                print(f"{i+1}.{item}")
            input("Selecione Enter para voltar ao menu anterior.")
    elif tarefa == 3:
    if not lista:
        print("Não há tarefas para remover.")
    else:
        for i, item in enumerate(lista):
            print(f"{i+1}.{item}")
        item_a_remover = int(input("Qual item você deseja remover?"))
        lista.pop(item_a_remover - 1)
        continuar = input("Deseja remover mais algum item?\nSelecione 6 para voltar ao menu anterior.")
        while continuar != '6':
            item_a_remover = int(input("Qual item você deseja remover?"))
            lista.pop(item_a_remover - 1)
            continuar = input("Deseja remover mais algum item?\nSelecione 6 para voltar ao menu anterior.")
    elif tarefa == 4:
        break
    else:
        print("Opção inválida.Selecione Enter para voltar ao menu anterior.")
        input("Selecione Enter para voltar ao menu anterior.")