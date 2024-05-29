# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# média abaixo de 5.0: REPROVADO
# média entre 5.0 e 6.9: RECUPERAÇÃO
# média 7.0 ou superior: APROVADO
#____________________________________________________________________________
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
média = (n1 + n2) / 2
if média < 5.0:
    print('Sua média foi {}, REPROVADO !'.format(média))
elif média >= 7.0:
    print ('Sua média foi {} APROVADO !'.format(média))
elif média >=5 and média < 7:
    print (' Sua média foi {}, RECUPERAÇÃO !'.format(média))