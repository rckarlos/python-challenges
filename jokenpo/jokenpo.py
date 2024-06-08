
# Jogo de pedra, papel e tesoura (computador vs usuário)
# Executado diretamente no terminal
# No final exibe estatísticas

from random import choice
a = True
emp = vit = der = 0
while a == True:
    lista = ['pedra', 'papel', 'tesoura']
    pc = choice(lista)
    b = True
    while b == True:
        user = input('Escolha pedra, papel ou tesoura: ').lower()
        if pc == user:
            print(f'O computador escolheu {pc}.')
            print('\033[33mEmpate.\033[m')
            emp += 1
            break
        elif (pc == 'pedra' and user == 'papel') or (pc == 'tesoura' and user == 'pedra') or (pc == 'papel' and user == 'tesoura'):
            print(f'O computador escolheu {pc}.')
            print('\033[32mVocê ganhou.\033[m')
            vit += 1
            break
        elif (pc == 'papel' and user == 'pedra') or (pc == 'pedra' and user == 'tesoura') or (pc == 'tesoura' and user == 'papel'):
            print(f'O computador escolheu {pc}.')
            print('\033[31mVocê perdeu.\033[m')
            der += 1
            break
        else:
            print('Digite um nome válido!')
    c = True
    while c == True:
        r = input('Deseja continuar [S/N]? ').upper()
        if r == 'S':
            break
        elif r == 'N':
            a = False
            break
        else:
            print('Inválido! Digite novamente.')
print('='*38)
print('--ESTATISTICAS--')
print(f'\033[33mEmpates: {emp}\033[m\n\033[32mVitorias: {vit}\033[m\n\033[31mDerrotas: {der}\033[m')
porVit = ((emp * 0.5 + vit) / (vit + emp + der) * 100)
print(f'Sua porcentagem de vitórias é de \033[32m{porVit:.1f}%')
