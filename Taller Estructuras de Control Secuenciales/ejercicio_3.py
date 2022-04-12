#Entradas
Venta1=int(input("Introduzca el valor de la primera venta: $"))
Venta2=int(input("Introduzca el valor de la segunda venta: $"))
Venta3=int(input("Introduzca el valor de la tercera venta: $"))
Sueldo_base=int(input("Introduzca el valor del sueldo devengado: $"))
#Caja negra
comision=(Venta1+Venta2+Venta3)*0.10
#Salidas
print("El sueldo devengado es: $",Sueldo_base)
print("La comision del mes es: $",comision)
print("El valor del sueldo total es de: $",Sueldo_base+comision)