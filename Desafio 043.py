# Deselvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu índice de Massa Corporal (IMC)
# e mostre seus status, de acordo com a tabela abaixo
# IMC abaixo de 18,5: Abaixo do peso
# Entre 18,5 e 25: Peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 30: Obesidade Mórbida
#____________________________________________________________________
peso = int(input(' Seu peso: '))
altura = float(input(' Sua altura: '))
imc = (peso / altura) /altura    # ou imc = peso / (altura ** 2)
if imc < 18.5:
    print(' Seu IMC é de {:.1f}, você está ABAIXO DO PESO !'.format(imc))
elif imc <= 25:
    print(' Seu IMC é de {:.1f}, seu peso está IDEAL !'.format(imc))
elif imc <= 30:
    print(' Seu IMC é de {:.1f}, você está SOBREPESO !'.format(imc))
elif imc <= 40:
    print(' Seu IMC é de {:.1f}, você está no estágio de OBESIDADE !'.format(imc))
    print('Precisa se cuidar !')
else:
    print(' Seu IMC é de {:.1f}, você está no estágio de OBESIDADE MÓRBIDA !'.format(imc))
    print('Precisa se cuidar !')
