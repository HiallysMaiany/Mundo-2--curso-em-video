# Escreva um programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base da conversão:

# 1 PARA BINÁRIO
# 2 PARA OCTAL
# 3 PARA HEXADECIMAL
numero = int(input('Escreva o número que deseja converter: '))
print('''ESCOLHA UMA DAS OPÇÕES PARA CONVERTER:
[ 1 ] CONVERTER PARA BINÁRIO
[ 2 ] CONVERTER PARA OCTAL
[ 3 ] CONVERTER PARA HEXADECIMAL''')
opção = int(input(' Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(numero,bin(numero) [2:]))
elif opção == 2:
    print ('{} convertido para OCTAL é igual a {}'.format(numero,oct(numero)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero) [2:]))
else:
    print ('Opção inválida. Tente novamente.')