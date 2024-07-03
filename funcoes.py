nome = input('Insira o seu nome: ')
idade = int(input('Insira a sua idade: '))

def nomeIdade(nome, idade):
    print(f'Olá, {nome} ano que vem, você faz {idade + 1} anos de idade.')
    return nome, idade

nomeIdade(nome, idade)