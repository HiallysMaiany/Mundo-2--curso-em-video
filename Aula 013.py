#ESTRUTURA DE REPETIÇÃO COM VARIÁVEL DE CONTROLE FOR

for c in range (1, 6):
    print('OI')
print('FIM')

#SE QUISER QUE A CONTAGEM SEJA PRA TRÁS:

for c in range (6, 0, -1):
    print(c)
print('FIM')

#PULANDO DE 2 EM 2:
for c in range (0, 7, 2):
    print(c)
print('FIM')

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range (i, f+1, p):
    print(c)
print('FIM')
