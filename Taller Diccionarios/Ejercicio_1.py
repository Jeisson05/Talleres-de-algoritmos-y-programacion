#Ejercicio1
Ejemplo=[12, 23, 5, 12, 92, 5, 12, 5, 29, 92, 64, 23]
Diccionario={}
for i in Ejemplo:
    a=Ejemplo.count(i)
    Diccionario.update({i:a})
print(Diccionario)