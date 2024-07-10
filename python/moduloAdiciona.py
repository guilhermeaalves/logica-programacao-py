import ex3 as ex

def adiciona_tarefa ():
    adicao_num = input('Digite um número para a sua tarefa: ')

    while adicao_num == '':
        respostaFinal = input('Você não digitou um número para classificar a sua tarefa, por favor digite um número para classificar a sua tarefa, digite 3 para encerrar ou digite 2 para voltar ao menu: ')
        adiciona_tarefa()
        break

    if adicao_tarefa or respostaFinal or adicao_num != '2':
        while adicao_num or adicao_tarefa or respostaFinal == '2':
            ex.menu_tarefas()
            break
        
    while adicao_num != '':
        adicao_tarefa = input('Digite a sua tarefa: ')
        break

    while adicao_num and adicao_tarefa != '2':
        ex.tarefas_dic[adicao_num] = adicao_tarefa
        adiciona_tarefa()
        break

    print(f'Sua tarefa foi adicionada com sucesso {ex.tarefas_dic}')

    ex.tarefas_dic.update({adicao_num : adicao_tarefa})
    print(f'Sua tarefa foi adicionada à lista com sucesso {ex.tarefas_dic}')

    respostaFinal = input('Você deseja adicionar mais alguma tarefa? Se sim digite: 1, se não digite: 2, caso você deseja voltar ao menu, digite: 3 > ')

