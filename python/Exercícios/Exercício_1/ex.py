numeros = []
pares = []
impares = []
entrada = input("Digite um número (ou 'sair' para encerrar o programa): ")

while entrada != 'sair':
        entrada = input("Digite um número (ou 'sair' para encerrar o programa): ")
        numero = int(entrada)
        numeros.append(numero)

for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    
print("Números pares ordenados:", pares)
print("Números ímpares ordenados:", impares)
    
soma_pares = sum(pares)
soma_impares = sum(impares)
    
print("Soma dos números pares:", soma_pares)
print("Soma dos números ímpares:", soma_impares)