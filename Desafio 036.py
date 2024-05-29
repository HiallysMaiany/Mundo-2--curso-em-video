# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado

casa = float (input('Qual o valor da casa ?'))
salário = float (input('Quanto é seu salário ?'))
anos = int(input('Em quantos anos você vai pagar a casa ?'))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print ('Para pagar uma casa de R${:.2f} em {} anos'.format (casa,anos))
print(' a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print ('Empréstimo pode ser CONCEDIDO !')
else:
    print('Empréstimo NEGADO !')
