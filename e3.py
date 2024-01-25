"""
Arnau Fernández Pinar
Matteo Vilchez
E3.Programa de traducció d’insults. Crear una estructura de dues dimensions amb els insults en català i afegir la traducció en castellà, anglès i klingon
El programa, demanarà a l’usuari que escrigui per teclat un insult, en català, i el mostrarà traduït a castellà, anglès i klingon.
23/01/2024
"""
try:
    Catalan=["capsigrany","borinot","mitja merda","figaflor"]
    Castellano=["alcaudón","moscardón","media mierda","breva"]
    Ingles=["shrike","blowfly","half a shit","breva"]
    Klingon=["mup","SuS","boD","Sep"]
    Insulto=str(input("Introduce un insulto: ")).lower()
    if Insulto in Catalan:
        index= Catalan.index(Insulto)
        print(Castellano[index],Ingles[index],Klingon[index])
    elif Insulto in Castellano:
        index2= Castellano.index(Insulto)
        print(Catalan[index2],Ingles[index2],Klingon[index2])
    elif Insulto in Ingles:
        index3= Ingles.index(Insulto)
        print(Catalan[index3],Castellano[index3],Klingon[index3])
    elif Insulto in Ingles:
        index4= Klingon.index(Insulto)
        print(Catalan[index4],Castellano[index4],Ingles[index4])
    else:
        print("No tiene traducción")
except:
    print("Error no Existe")
