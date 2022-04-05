Algoritmo Suma_multiplicación_resta_y_división
	Escribir "Ingrese un valor a: "
	Leer a
	Escribir "Ingrese un valor b: "
	Leer b
	suma<-a+b
	resta<-a-b
	multiplicación<-a*b
	Si b=0 Entonces
		división<-0
	SiNo
		división<-a/b
	Fin Si
	Escribir "El resultado de la suma es: " suma
	Escribir "El resultado de la resta es: " resta
	Escribir "El resultado de la multiplicación es: " multiplicación
	Escribir "El resultado de la división es: " división
FinAlgoritmo