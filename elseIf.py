nome = "Guilherme Alves"
idade = 17
peso = 75
altura = 1.78

filmes = {
    1 : "Homem Aranha no aranha verso",
    2 : "Vingadores Ultimato",
    3 : "Besouro Azul"
}

print(nome, idade, peso, altura, filmes)

idade = input("Insira a sua idade: ")
idade = int(idade)

if idade >= 18:
    print('Maior de idade')
elif idade == 16:
    print('Deve apresentar um documento com foto do responsável')
else:
    print('É menor de idade')

opcao = ''

while opcao != 'sair':
    opcao = input('Digite sair para sair: ')



    
