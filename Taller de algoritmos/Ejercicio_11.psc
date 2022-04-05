Algoritmo Calificación_final
	Escribir "Escriba las tres notas: "
	Leer Nota_1, Nota_2, Nota_3
	Escribir "Escriba la nota del examen_final: "
	Leer examen_final
	Escribir "Escriba la nota del trabajo_final: "
	Leer trabajo_final
	Promedio<-(Nota_1+Nota_2+Nota_3)/3
	Nota_final<-(promedio*0.55)+(examen_final*0.30)+(trabajo_final*0.15)
	Escribir "La nota final del estudiante es: " Nota_final
FinAlgoritmo