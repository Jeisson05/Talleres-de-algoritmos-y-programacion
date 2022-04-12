#Entradas
Chelines_austriacos=int(input("Introduzca la cantidad de chelines austriacos: $"))
Dracmas_griegos=int(input("Introduzca la cantidad de dracmas griegos: $"))
Pesetas=int(input("Introduzca la cantidad de pesetas: $"))
#Caja negra
Pesetas=Chelines_austriacos*9568.71
Franco_frances=Dracmas_griegos*(886.07/20110)
Dolar_EEUU=Pesetas*0.00000816
Liras_italianas=Pesetas*0.01076542
#Salidas
print("Una peseta equivale a: $",round(Pesetas,2)) 
print("Un franco frances equivale a: $",round(Franco_frances,2))
print("Un dolar EEIUU equivale a: $",round(Dolar_EEUU,2))
print("Una lira italiana equivale a: $",round(Liras_italianas,2))