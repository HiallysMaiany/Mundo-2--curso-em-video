# Crie um programa que mostre na tela todos os números 
# pares que estão no intervalo entre 1 e 50.

for n in range (1, 51):       # Ou (2, 51, 2):
    if n % 2 == 0:
       print(n, end= ' ')     # O " end " serve para visualizar tudo escrito em uma única linha.
print(' ✨ ACABOU !🎉')
