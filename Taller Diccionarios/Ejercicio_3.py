usuarios = {
        "iperurena": {
            "nombre": "Iñaki",
            "apellido": "Perurena",
            "password": "123123"
    },
        "fmuguruza": {
            "nombre": "Fermín",
            "apellido": "Muguruza",
            "password": "654321"
    },
        "aolaizola": {
            "nombre": "Aimar",
            "apellido": "Olaizola",
            "password": "123456"
    }
 }

Usuario=str(input("Escriba su usuario: "))
Contraseña=int(input("Escriba su contraseña: "))
cont=0
for clave in usuarios:
    if Usuario in usuarios.keys() and Contraseña in usuarios.values()==True:
       print("Contraseña correcta")
    else:
        if Usuario in usuarios.keys() and Contraseña in usuarios.values()==False:
            print("Contraseña incorrecta")
        intentos=cont+1
        print("Este es su primer intento.",intentos)
        if Usuario in usuarios.keys() and Contraseña in usuarios.values()==False:
            print("Contraseña incorrecta")
        intentos=cont+1
        print("Este es su segundo intento.",intentos)   
        if Usuario in usuarios.keys() and Contraseña in usuarios.values()==False:
            print("Contraseña incorrecta")
        intentos=cont+1
        print("Este es su tercer intento.",intentos)
        print("Demasiados intentos")