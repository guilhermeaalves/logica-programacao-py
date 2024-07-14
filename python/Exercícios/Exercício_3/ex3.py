import moduloMenu as menu

tarefas_dic = {}

menu

def menu_tarefas ():

    while True:
        opcao = input('Selecione uma opção: ')

        if opcao == '1':
            print('\033[32mAdicionar Tarefa selecionada.\033[0m')
            adiciona_tarefa()
            
        elif opcao == '2':
            print('\033[31mRemover Tarefa selecionada.\033[0m')
            remove_tarefa()
            
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

def adiciona_tarefa ():
    # adicao_num = input('Digite um número para a sua tarefa: ')


    # while adicao_num == '':
    #     while resposta != '3':
    #         resposta = input('Você não digitou um número para classificar a sua tarefa, por favor digite um número para classificar a sua tarefa, digite 3 para encerrar ou digite 2 para voltar ao menu: ')
    #         adiciona_tarefa()
    #         break
        
    # while adicao_num != '':
    #     adicao_tarefa = input('Digite a sua tarefa: ')
    #     break
    
    # while adicao_tarefa != '':
    #     tarefas_dic[adicao_num] = adicao_tarefa
    #     print(f'\033[32mTarefa adicionada com sucesso!{tarefas_dic}\033[0m')
    #     break

    # respostaFinal = input('Você deseja adicionar mais alguma tarefa? Se sim digite: 1, se não digite: 2, caso você deseja voltar ao menu, digite: 3 > ')

    # while respostaFinal and resposta == '1':
    #     adiciona_tarefa()
    #     break
    # while respostaFinal == '2':
    #     break
    # while respostaFinal and resposta == '3':
    #     menu
    #     menu_tarefas()
    #     break

    while True:
        adicao_num = input('Digite um número para a sua tarefa: ')

        if adicao_num == '':
            print('\033[31mVocê não digitou um número para classificar a sua tarefa, por favor digite um número para classificar a sua tarefa ou, digite sair para encerrar o programa ou digite menu para voltar ao menu: \033[0m')
        if adicao_num == 'sair':
            break
        elif adicao_num == 'menu':
            menu_tarefas()
            break
        
        else:
            adicao_tarefa = input('Digite a sua tarefa: ')
            tarefas_dic[adicao_num] = adicao_tarefa
            print(f'\033[32mTarefa adicionada com sucesso!{tarefas_dic}\033[0m')
            

            if adicao_tarefa != '':
                tarefas_dic.update({adicao_num : adicao_tarefa})

            if adicao_tarefa == '':
                print('\033[31mVocê não digitou uma tarefa, por favor digite uma tarefa para adicionar, ou digite 3 para encerrar ou digite 2 para voltar ao menu: \033[0m')
                adiciona_tarefa()
                break

            elif adicao_tarefa == 'sair':
                break

            elif adicao_tarefa == 'menu':
                menu_tarefas()
                break

def remove_tarefa ():
    print (tarefas_dic)
    rm = input('Digite um número de qual tarefa você deseja remover: ')

    while rm != '2':
        remove_tarefa()
        print(f'Sua tarefa foi removida com sucesso {tarefas_dic}')
        break
    
    while rm == '':
        print('Você não digitou um número para remover uma tarefa, por favor digite um número para classificar a sua tarefa, ou digite sair, para encerrar o programa: ')

    tarefas_dic.pop(rm)

    respostaFinal = input('Você deseja remover mais alguma tarefa? Se sim digite: 1, se não digite: 2, caso você deseja voltar ao menu, digite: 3 > ')

    while respostaFinal == '1':
        remove_tarefa()
        break
    while respostaFinal == '3':
        menu_tarefas()
        break

menu_tarefas ()
