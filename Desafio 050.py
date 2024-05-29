# Desenvolva um programa que leia seis números inteiros e mostre a soma
# apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
soma_pares = 0
for n in range (1, 7):
    numero = int(input('Escreva o {} valor: '.format(n)))
    print(n)
    soma_pares += numero 
if numero % 2 == 0:
    print('A soma dos números pares é {}'.format (soma_pares))
else:
    print('OS NÚMEROS NÃO SÃO PARES')

        
    