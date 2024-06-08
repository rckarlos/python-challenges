
# Manipulação de listas
# Dividindo uma lista em duas sublistas de números pares e ímpares

# Funções
# Ordenar a lista sem usar o método sort()

def bubbleSort(lista):
    tamanho = len(lista)-1
    for j in range(tamanho):
        for i in range(tamanho):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
    return lista


# Converter a lista para string e remover colchetes

def listToString(lista):
    string = ', '.join(map(str, lista))
    return string

listaOriginal, listaPares, listaImpares = [], [], []

while True:
    valor = int(input('Digite um valor: '))
    listaOriginal += [valor]
    if valor % 2 == 0:
        listaPares.append(valor)
    else:
        listaImpares.append(valor)

    while True:
        usuario = input('Deseja continuar [S/N]? ').upper()
        if usuario == 'S':
            break
        elif usuario == 'N':
            break
        else:
            print('\033[31mResposta inválida.\033[m')

    if usuario == 'N':
        break
    
print('-' * 38)
print(f'Lista completa: {listToString(listaOriginal)}.')
print(f'Lista com somente números pares: {listToString(listaPares)}.')
print(f'Lista com somente números ímpares: {listToString(listaImpares)}.')
print('-' * 38)
print(f'Lista completa \033[32morganizada\033[m: {listToString(bubbleSort(listaOriginal))}.')
print(f'Lista \033[32morganizada\033[m com somente números pares: {listToString(bubbleSort(listaPares))}.')
print(f'Lista \033[32morganizada\033[m com somente números ímpares: {listToString(bubbleSort(listaImpares))}.')