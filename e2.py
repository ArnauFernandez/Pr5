"""
Arnau Fernández Pinar
Matteo Vilchez
E2.Programa que generi una llista de 100 nombres aleatoris entre 1 i 50. 
Obtenir la mitja dels nombres que es troben a les posicions parelles i la mitja del nombre de les posicions senars. 
23/01/2024
"""

import random
MEDIDA=100
Numeros=[]
for i in range(MEDIDA):
    Numeros.insert(1, random.randint(1,50))
print("La media del numero de las posiciones parelles: ",sum(Numeros[0::2])/50)
print("La media del numero de las posiciones senars: ",sum(Numeros[1::2])/50)
