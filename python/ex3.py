import moduloMenu as menu
import moduloAdiciona as add
import moduloRemove as rm

tarefas_dic = {}

menu

def menu_tarefas ():

    while True:
        opcao = input('Selecione uma opção: ')

        if opcao == '1':
            print('\033[32mAdicionar Tarefa selecionada.\033[0m')
            add.adiciona_tarefa()
            
        elif opcao == '2':
            print('\033[31mRemover Tarefa selecionada.\033[0m')
            rm.remove_tarefa()
            
        elif opcao == '3':
            print('\033[32mMarcar Uma Tarefa Como Concluída selecionada.\033[0m')
            
        elif opcao == '4':
            print('\033[36mListar Todas as Tarefas selecionada.\033[0m')
           
        elif opcao == '5':
            print('\033[32mListar Tarefas Concluídas selecionada.\033[0m')
            
        elif opcao == '6':
            print('\033[33mListar Tarefas Não Concluídas selecionada.\033[0m')
            
        elif opcao == '7':
            print('\033[31mSaindo...por isso a média do qi brasileiro é de 83 pontos\033[0m')
            break
        else:
            print('\033[31mOpção inválida. Tente novamente, ou digite 7 para sair.\033[0m')

menu_tarefas () 
