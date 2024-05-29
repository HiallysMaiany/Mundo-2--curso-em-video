# ESTRUTURA DE REPETIÇÃO COM TESTE LÓGICO:

# enquanto não 🍎          /     while not 🍎:
#      passo              /          passo
# pega                   /       pega

c = 1
while c < 10:
    print(c)
    c = c + 1
print ('Fim')

# O WHILE É USADO QUANDO NÃO SABEMOS UM LIMITE, EXEMPLO:

n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print ('FIM')

# LAÇOS INDETERMINADOS:

r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]' )).upper()
print|('FIM')