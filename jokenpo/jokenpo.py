
# Jogo de pedra, papel e tesoura (computador vs usuário)
# Executado diretamente no terminal
# No final exibe estatísticas

from random import choice

empates, vitorias, derrotas = 0, 0, 0

while True:
    pc = choice(['pedra', 'papel', 'tesoura'])

    while True:
        user = input('Escolha pedra, papel ou tesoura: ').lower()
        if user in ['pedra', 'papel', 'tesoura']:
            break
        else:
            print('Digite uma escolha válida!')

    if pc == user:
        print(f'O computador escolheu {pc}.')
        print('\033[33mEmpate.\033[m')
        empates += 1
    elif (pc == 'pedra' and user == 'papel') or \
         (pc == 'tesoura' and user == 'pedra') or \
         (pc == 'papel' and user == 'tesoura'):
        print(f'O computador escolheu {pc}.')
        print('\033[32mVocê ganhou.\033[m')
        vitorias += 1
    else:
        print(f'O computador escolheu {pc}.')
        print('\033[31mVocê perdeu.\033[m')
        derrotas += 1

    while True:
        continuar = input('Deseja continuar [S/N]? ').upper()
        if continuar == 'N':
            break
        elif continuar == 'S':
            break
        else:
            print('Inválido! Digite novamente.')
    
    if continuar == 'N':
        break

print('='*38)
print('--ESTATISTICAS--')
print(f'\033[33mEmpates: {empates}\033[m\n\033[32mVitorias: {vitorias}\033[m\n\033[31mDerrotas: {derrotas}\033[m')
totalJogos = vitorias + empates + derrotas
porcentagemVitorias = ((vitorias + empates) / totalJogos) * 100
print(f'Sua porcentagem de vitórias é de \033[32m{porcentagemVitorias:.1f}%\033[m')
