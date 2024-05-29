# A confederação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# Até 9 anos: MIRIM
# Até 14 anos: INFANTIL
# Até 19 anos: JÚNIOR
# Até 25 anos: SÊNIOR
# Acima de 25 anos: MASTER
#____________________________________________________________________________________________
from datetime import date
ano = int(input(' Ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print (' Você tem {} anos e competirá na categoria MIRIM'.format(idade))
elif idade >=10 and idade <=14:
    print (' Você tem {} anos e competirá na categoria INFANTIL'.format(idade))
elif idade >= 15 and idade <= 19:
    print(' Você tem {} anos e competirá na categoria JÚNIOR'.format(idade))
elif idade >= 20 and idade <= 25:
    print( 'Você tem {} anos e competirá na categoria SÊNIOR '.format(idade))
elif idade > 25:
    print(' Você tem {} anos e competirá na categoria MASTER'.format(idade))
    