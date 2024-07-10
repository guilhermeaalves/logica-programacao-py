# menu = {
#        'Menu' : '',
#        1. : 'Adicionar Tarefa',
#        2. : 'Remover Tarefa',
#        3. : 'Marcar Uma Tarefa Como Concluída',
#        4. : 'Listar Todas as Tarefas',
#        5. : 'Listar Tarefas Concluídas',
#        6. : 'Listar Tarefas Não Concluídas',
#        7. : 'Sair'
# }

# print(menu)

print('''
       Menu:
       1. Adicionar Tarefa
       2. Remover Tarefa
       3. Marcar Uma Tarefa Como Concluída
       4. Listar Todas as Tarefas
       5. Listar Tarefas Concluídas
       6. Listar Tarefas Não Concluídas
       7. Sair''')


tarefas_dic = {}

def menu_tarefas ():
    opcao = input('Escolha uma opção: ')

    while opcao == 'sair':
        menu_tarefas()
        break
    if opcao == '1':
        adiciona_tarefa()
    elif opcao == '2':
        remove_tarefa()


def remove_tarefa ():
    print (tarefas_dic)
    rm = input('Digite o número de qual tarefa você deseja remover: ')

    while rm != 'sair':
        remove_tarefa()
        break
    print(f'Sua tarefa foi removida com sucesso {tarefas_dic}')

    tarefas_dic.pop(rm)

    respostaFinal = input('Você deseja remover mais alguma tarefa? Se sim digite: 1, se não digite: 2, caso você deseja voltar ao menu, digite: 3')

    while respostaFinal != '2':
        remove_tarefa()
        break
    while respostaFinal == '3':
        menu_tarefas()
        break

    # tarefas.

def adiciona_tarefa ():
    adicao_num = input('Digite o número para classificar a sua tarefa: ')
    adicao_tarefa = input('Digite o nome da tarefa para adicionar: ')

    if adicao_num == '':
        while adicao_num == '':
            adicao_num
    else
        while 

    tarefas_dic.update({adicao_num : adicao_tarefa})
    print(f'Sua tarefa foi adicionada à lista com sucesso {tarefas_dic}')

menu_tarefas () 