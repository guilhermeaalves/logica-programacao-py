import moduloAdiciona as add
import ex3 as menu

def remove_tarefa ():
    print (menu.tarefas_dic)
    rm = input('Digite um número de qual tarefa você deseja remover: ')

    while rm != '2':
        remove_tarefa()
        print(f'Sua tarefa foi removida com sucesso {menu.tarefas_dic}')
        break
    
    while rm == '':
        print('Você não digitou um número para remover uma tarefa, por favor digite um número para classificar a sua tarefa, ou digite sair, para encerrar o programa: ')

    menu.tarefas_dic.pop(rm)

    respostaFinal = input('Você deseja remover mais alguma tarefa? Se sim digite: 1, se não digite: 2, caso você deseja voltar ao menu, digite: 3 > ')

    while respostaFinal == '1':
        remove_tarefa()
        break
    while respostaFinal == '3':
        menu.menu_tarefas()
        break


    def volta_menu ():
        if respostaFinal == '1':
            add.adiciona_tarefa()
        elif respostaFinal == '3':
            menu.menu_tarefas()
        
    volta_menu()