produtos = {
        "celular" : 1500.00,
        "câmera" : 1000.00,
        "fone de ouvido" : 800.00,
        "monitor" : 2000.00
    }

print(f'Esses são os produtos disponíveis: {produtos}')

def cadastra_produto():
        cadastro = input("Você deseja cadastrar um produto? ")
        if cadastro == "sim":
            while cadastro != "":
                cadastro = input("Digite o nome do produto: ")
                break
            valor = int(input("Digite o valor do produto: "))
            while valor != "": 
                produtos[cadastro] = valor
                break
            print(f'Seu produto foi adicionado à lista com sucesso {produtos}')
        else:
            print("Obrigado por utilizar o sistema, seu animal.")

def encontra_produto():
    entrada = input("Qual produto você deseja? ").lower()

    if entrada in produtos:
        print(f'O valor do produto {entrada} é {produtos[entrada]}')
    else:
        while entrada not in produtos:
            print("Produto não encontrado tente novamente")
            entrada = input("Digite o nome de produto para ver o preço: ")
            break
        cadastra_produto()
        
encontra_produto()