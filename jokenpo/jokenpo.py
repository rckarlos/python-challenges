
# Jogo de pedra, papel e tesoura (computador vs usuário)
# Executado diretamente no terminal
# No final exibe estatísticas

from random import choice

empates, vitorias, derrotas = 0, 0, 0

print('Vamos brincar de pedra papel e tesoura?\n')

while True:
    pc = choice([1, 2, 3])
    print('''ESCOLHA UM NÚMERO
\033[34m[1]\033[m PEDRA
\033[34m[2]\033[m PAPEL
\033[34m[3]\033[m TESOURA
\033[31m[4]\033[m CANCELAR''')
    
    while True:
        user = int(input(''))
        if 1 <= user <= 3:
            break
        elif user == 4:
            break
        else:
            print('\033[31mDigite um número válido!\033[m')

    if user == 4:
        break

    print(f'O computador escolheu \033[34m{pc}\033[m.')

    if pc == user:
        print('\033[33mEmpate!\033[m\n')
        empates += 1
    elif (pc == 1 and user == 2) or\
        (pc == 2 and user == 3) or\
        (pc == 3 and user == 1):
        print('\033[32mVocê venceu!\033[m\n')
        vitorias += 1
    else:
        print('\033[31mVocê perdeu.\033[m\n')
        derrotas += 1


print('='*38)
print('--ESTATISTICAS--')
print(f'''\033[33mEmpates: {empates}\033[m
\033[32mVitorias: {vitorias}\033[m
\033[31mDerrotas: {derrotas}\033[m''')
totalJogos = vitorias + empates + derrotas
porcentagemVitorias = ((vitorias + (empates * 0.5)) / totalJogos) * 100
print(f'Sua porcentagem de vitórias é de \033[32m{porcentagemVitorias:.1f}%\033[m')
