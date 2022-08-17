#CONDICIONAIS
'''
Eu cheguei atrasado na aula,ainda posso entrar?
Se essa não for sua terceira vez chegando atrasado,então pode sim,caso
contrário irá tomar uma suspensão.
'''
numero_de_atrasos = 3
if numero_de_atrasos >=3:
   print('Você está suspenso!')
elif numero_de_atrasos == 1:
   print('Pode entrar,mas se tomar mais 2 faltas,irá ser suspenso')
elif numero_de_atrasos == 2:
   print ('Pode entrar,mas se tomar mais 1 faltas,irá ser suspenso')
else:
   print('Pode entrar')
