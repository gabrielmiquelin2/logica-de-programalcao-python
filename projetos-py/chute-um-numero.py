#PROJETO - CHUTE UM NÚMERO
'''
Escreva um programa que,ao iniciar gera um valor aleatório de 1a 10 e
permite que o usuário chute um número até que o valor aleatório gerado no
início do programa seja chutado corretamente.

O programa deve informar se o chute foi acima,abaixo ou igual ao valor
aleatório gerado no início do programa.  

#Método 5Q's para montar um algorítimo:

Analise criticamente o problema e descubra:
(Tente explicar este problema para você mesmo em voz altaepeça mais
informações/investigue mais até você compreender completamente o problema.)

1. Quais são os dados de entrada necessários?
valor aleatório de 1a 10 
-Chute do usuário
2.Oque devo fazer com estes dados?
Eu devo comparar o chute do usuário com o valor aleatório que foi gerado no inicio do programa e dezer
se o chute for maio, menor ou igual ao valor que foi gerado no inicio do programa

3. Quais são as restrições deste problema?
-Um valor aleatório  de 1 a 10

4. Qual é o resultado esperado?
O programa deve informar se o chute foi acima,abaixo ou igual ao valor
aleatório gerado no início do programa.  

5. Qual é sequência de passos a ser feitas para chegar ao resultado esperado?

input valor_aleatorio de 1 a 10 
input chute 
if chute > valor_aleatorio:
    print("Chute foi maior que o valor gerado")
if chute < valor_aleatorio
   print ("Chute foi menor que o valor gerado")
if chute = valor_aleatorio
   print("Você Acertou!")

'''


import random  #biblioteca random serve para gerar um valor aleatório no python

valor_aleatorio = random.randint(1,10) #GEREI UM VALOR ALEATÓRIO DE 1 a 10
acertou = False
while acertou == False:
  chute = int(input('Chute um valor de 1 a 10: '))
  if chute > valor_aleatorio:
    print('Chute foi maior que o valor gerado')
  elif chute < valor_aleatorio:
    print('Chute foi menor que o valor gerado')
  elif chute == valor_aleatorio:
    acertou = True
    print('Você acertou!')
