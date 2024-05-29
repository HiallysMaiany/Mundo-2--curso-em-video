# Faça um programa que calcule a soma entre todos os números 
# que são múltiplos de três e que se encontram no intervalo até 500.
#___________________________________________________________________
soma = 0
cont = 0
for n in range (1, 501, 2):
    if n % 3 == 0:
     soma = soma + n
     cont = cont + 1
     print(n) 
print('A soma de todos os {} números múltiplos de três no intervalo de 1 a 500 é {}'.format (cont,soma))