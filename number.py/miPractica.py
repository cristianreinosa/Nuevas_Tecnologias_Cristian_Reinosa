# Generar un programa que permita hacer el registro e iniciar sesion dentro de while, debe imprimir el menu usando la implementacion de if, elif, else (Selector multiple).cuandoinicie sesion que implemente la solucion del calculo de cuotas creada en el reto anterior.
usuarios_registrados = {}

nombre = input("Ingrese su nombre")
contraseña = int(input("Ingrese su contraseña"))

if(nombre == "cristian" and contraseña == 12345):
    print("Usuario registrado con exito")
else:
    print("Nombre O Contraseña incorrectos")   
        