
# Algoritmo que descobre se o número digitado pelo usuário é primo

# Funções
# Calcular se um número é primo ou não

def numeroPrimo(valor):
    if valor <= 1:
        return False
    for i in range(2, valor):
        if valor % i == 0:
            return False
    return True

totalPrimos = 0

while True:
    valor = int(input('Digite um valor: '))
    if numeroPrimo(valor):
        print(f'{valor}\033[32m é\033[m um número primo')
        totalPrimos += 1
    else:
        print(f'{valor}\033[31m não é\033[m um número primo')

    while True:
        continua = input('Quer digitar outro número [S/N]? ').upper()
        if continua == 'S':
            break
        elif continua == 'N':
            break
        else:
            print('\033[31mDigite uma resposta válida!\033[m')

    if continua == 'N':
        break
print('-'*38)
print(f'Total de números primos digitados: {totalPrimos}')