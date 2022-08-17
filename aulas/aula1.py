from errno import EDEADLK


#Variáveis

#Números
velocidade_internet = 10
print(velocidade_internet)
nota_filme = 8.5 #float

#Valores boleanos
esta_aberto = True

#Strings
nome_do_curso = 'Lógica de programação'

#Como variáveis seriam usasdo em um progrmaa real?
#Problema 1 - valor por hora
#Escreva um programa que retorna o valor hora de um funcionário
#com base no seu saláario mensal e horas trabalhadas por mes.

#PSEUDOCÓDIGO
'''
input salario_mensal
input horas_trabalhada_por_mes
valor_hora = salario_mensal / horas_trabalhadas_por_mes
print valor_hora
'''
#AGORA ESSES MESMO CÓDIGO EM LINGUAGEM PYTHON
salario_mensal = input('Qual  o seu salário mensal?')
horas_trabalhadas_por_mes = input('Quantas horas trabalhadas por mês?')
valor_hora = int (salario_mensal) / int (horas_trabalhadas_por_mes)     #int = numero inteiro
print (valor_hora)