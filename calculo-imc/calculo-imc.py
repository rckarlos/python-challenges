
# Calculadora de Índice de Massa Corporal

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

if altura > 100:
    altura = altura/100

calculoIMC = peso/altura ** 2

if calculoIMC < 18.5:
    print(f'Seu IMC é {calculoIMC:.1f} e você está abaixo do peso.')
elif 25 > calculoIMC >= 18.5:
    print(f'Seu IMC é {calculoIMC:.1f} e você está no peso ideal.')
elif 30 > calculoIMC >= 25:
    print(f'Seu IMC é {calculoIMC:.1f} e você está acima do peso.')
elif 40 > calculoIMC >= 30:
    print(f'Seu IMC é {calculoIMC:.1f} e você está com obesidade.')
else:
    print(f'Seu IMC é {calculoIMC:.1f} e você está com obesidade mórbida.')
