#Entradas
Horas_laboradas=int(input("Ingrese la cantidad de horas laboradas: "))
Valor_hora=int(input("Ingrese el valor devengado por hora: "))
#Caja negra
Sueldo_base=Horas_laboradas*Valor_hora
Descuento=Sueldo_base*0.2
Sueldo_neto=Sueldo_base-Descuento
#Salidas
print("El sueldo neto devengado, es de: $",Sueldo_neto)