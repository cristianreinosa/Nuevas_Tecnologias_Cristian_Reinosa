registro = {
    "name" : "cristian",
    "imail" : "crisdavid@gmail.com",
    "clave" : 1234
}


usuario = input("Ingrese su usuario o su numero de telefono")
clave = int(input("Ingrese su clave"))
captcha = input("cual es su animal favorito")

if((usuario == registro["name"]) or (usuario == "506789") and clave == registro["clave"] and captcha == "peter"):
    print("Ingreso exitoso")
else:
    print("Usuario y Clave son incorrectos")    
