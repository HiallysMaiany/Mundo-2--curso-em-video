# Refaça o DESAFIO 9, mostrando a tabuada de um número
#que o usuário escolher, só que agora utilizando um laço for.
#____________________________________________________________

n = int(input('Digite um número para ver sua tabuada: '))
for tab in range (1 , 11 ):
    m = tab * n
    print('{} x {} : {}'.format(n, tab, m))
