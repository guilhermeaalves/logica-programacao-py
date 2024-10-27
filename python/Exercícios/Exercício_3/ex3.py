import json
import moduloMenu as menu

def abrirArquivo(nomeArquivo):
    try:
        with open(nomeArquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo não encontrado.')
        return {}
    
def salvarArquivo(nomeArquivo, dados):
    with open(nomeArquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)

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
            tarefa_concluida()

            
        # elif opcao == '4':
        #     print('\033[36mListar Todas as Tarefas selecionada.\033[0m')
           
        # elif opcao == '5':
        #     print('\033[32mListar Tarefas Concluídas selecionada.\033[0m')
            
        # elif opcao == '6':
        #     print('\033[33mListar Tarefas Não Concluídas selecionada.\033[0m')
            
        # elif opcao == '7':
        #     print('\033[31mSaindo...por isso a média do qi brasileiro é de 83 pontos\033[0m')
        #     break
        else:
            print('\033[31mOpção inválida. Tente novamente, ou digite 7 para sair.\033[0m')


def adiciona_tarefa ():

    try:
        nomeArquivo = 'python/Exercícios/Exercício_3/dados.json'
        dados = abrirArquivo(nomeArquivo)

        adicao_num = input('Digite um número para a sua tarefa: ')
        adicao_tarefa = input('Digite a descrição da sua tarefa: ')
        adicao_status = input('Digite um status para a sua tarefa: ')

        if adicao_num in dados:
            print("\033[31mErro: Tarefa com este número já existe.\033[0m")
        
        dados[int(adicao_num)] = adicao_tarefa, adicao_status
        salvarArquivo(nomeArquivo, dados)
        print(f"\033[32mTarefa {adicao_tarefa} adicionada com sucesso!\033[0m")

    except ValueError:

        print('\033[31mErro: Número inválido.\033[0m')
        
    except Exception as e:

        print(f"\033[31mErro ao adicionar tarefa: {e}\033[0m")

    finally:
        menu_tarefas()

def remove_tarefa ():

    nomeArquivo = 'python/Exercícios/Exercício_3/dados.json'
    
    dados = abrirArquivo(nomeArquivo)

    if not dados:
        print("Nenhuma tarefa encontrada.")
        return menu_tarefas()

    print("\nTarefas atuais:")
    for num, descricao, status in dados.items():
        print(f"{num}. {descricao} {status}")

    try:
        rm = int(input('Digite o número da tarefa que você deseja remover: '))
        rm_str = str(rm)

        if rm_str not in num:
            print("\033[31mErro: Número inválido.\033[0m")
        else:
            dados.pop(str(rm))
            salvarArquivo(nomeArquivo, dados)
            print("\033[32mTarefa removida com sucesso!\033[0m")

    except ValueError:
        print("\033[31mErro: Número inválido.\033[0m")

    except Exception as e:
        print("\033[31mErro ao remover tarefa: {e}\033[0m")

def tarefa_concluida ():
        
    nomeArquivo = 'python/Exercícios/Exercício_3/dados.json'
    
    dados = abrirArquivo(nomeArquivo)

    if not dados:
        print("Nenhuma tarefa encontrada.")
        return menu_tarefas()

    print("\nTarefas atuais:")
    for num, descricao in dados.items():
        print(f"{num}. {descricao}")

        
        try:
            st = int(input('Digite o número da tarefa a ser concluída: '))
            dados.get(st)
            if st == 'concluida':
                print("\033[31mErro: tarefa já está marcada como concluída.\033[0m")

        except ValueError:
            print("\033[31mErro: Número inválido.\033[0m")

    
menu_tarefas()