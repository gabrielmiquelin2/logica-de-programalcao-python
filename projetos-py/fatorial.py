'''
Crie um programa que receber um número e imprime o seu fatorial
daquele número
#Método 5Q's para montar um algorítimo:
Analise criticamenteoproblemaedescubra:
(Tente explicar este problema para você mesmo em voz altae
peça mais informações/investigue mais até você compreender
completamenteoproblema.)

5QS:
1. Quais são os dados de entrada necessários?
numero

2.Oque devo fazer com estes dados?
eu devo calcular o fatorial do numero que for passado para o meu programa e o exibir na tela.

3. Quais são as restrições deste problema?
-O número Deve ser um valor positivo
-O número Deve ser um valor inteiro

4. Qualéoresultado esperado?
-O resultado esperado é que o fatorial do numero providenciado seja exibido

5. Qual é sequência de passosaser feitas para chegar ao
resultado esperado?
#pseudocódigo
input numero
if numero > 0
if numero = inteiro
fatorial = 1
loop de 1 a numero
   fatorial = fatorial * numero
print(fatorial)
'''

numero = int (input('Digite um numero'))
if numero > 0:
    fatorial = 1
    for item in range (1,numero +1):
       fatorial = fatorial * item
print(fatorial)
