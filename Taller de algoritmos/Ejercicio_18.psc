Algoritmo Iniciales_nombre_y_apellido
	Escribir "Escriba su nombre, su primer apellido y su segundo apellido: "
	Leer nombre, primer_apellido, segundo_apellido
	Inicial_nombre<-Subcadena(nombre,1,1)
	Inicial_primer_apellido<-Subcadena(primer_apellido,1,1)
	Inicial_segundo_apellido<-Subcadena(segundo_apellido,1,1)
	Escribir Mayusculas(Inicial_nombre), Mayusculas(Inicial_primer_apellido), Mayusculas(Inicial_segundo_apellido)
FinAlgoritmo