#Entradas
Nota1=int(input("Digite el valor de la primera nota: "))
Nota2=int(input("Digite el valor de la segunda nota: "))
Nota3=int(input("Digite el valor de la tercera nota: "))
Examen_final=int(input("Digite el valor de la nota del examen final: "))
Trabajo_final=int(input("Digite el valor de la nota del trabajo final: "))
#Caja negra
Promedio=(Nota1+Nota2+Nota3)/3
Nota_final=(Promedio*0.55)+(Examen_final*0.30)+(Trabajo_final*0.15)
print("La nota final del estudiante es: ",round(Nota_final,2))