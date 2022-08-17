#CONDICIONAIS
#if.elif e else

#Encontre o mair entre 2 números
#EXEMPLO EM PSEUDOCÓDIGO
'''
input primeiro valor
input segundo valor
if primeiro valor>segundo_valor
    printoprimeiro valorémaior
else
   printosegundo valorémaior
'''

primeiro_valor = input('Digite o 1º valor:')
segundo_valor = input('Digite o 2º valor:')

if int(primeiro_valor) > int (segundo_valor):
   print('O primeiro valor é maior!')
else:
   print('O segundo valor é maior!')   