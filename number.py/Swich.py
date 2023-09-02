# print("1. Registro \n 2. login \n 3. Salir")

# opc = 0

# if opc == 1:
#     print("Registro")
# elif opc == 2:
#     print("login")
# elif opc == 3:
#     print("Salir")
# else:
#     print("Seleccione una Opcion valida")


# Generar un programa que permita hacer el registro e iniciar sesion dentro de while, debe imprimir el menu usando la implementacion de if, elif, else (Selector multiple).cuandoinicie sesion que implemente la solucion del calculo de cuotas creada en el reto anterior.

usuarios_registrados = {}

# Función para registrar un nuevo usuario
def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    contraseña = input("Ingrese su contraseña: ")
    usuarios_registrados[nombre] = contraseña 
    print("Usuario registrado exitosamente.")

# Función para iniciar sesión
def iniciar_sesion():
    nombre = input("Ingrese su nombre: ")
    contraseña = input("Ingrese su contraseña: ")
    if usuarios_registrados.get(nombre) == contraseña:
        print("Inicio de sesión exitoso.")
        return True
    else:
        print("Nombre de usuario o contraseña incorrectos.")
        return False

# Función para calcular cuotas de compra
def calcular_cuotas():
    compra = float(input("ingrese el valor de la compra"))
    cuotas = int(input("ingrese el numero de cuotas"))
    valor = compra / cuotas
    print("total de la cuota es",valor)
    cuotaActual = 1
    saldoPendiente = compra
    while  cuotaActual <= cuotas:
        print("Cuota ",cuotaActual,"\n valor de cuota ",valor," \n Saldo restante",saldoPendiente,"\n Cuotas canceladas ")
        cuotaActual+=1
        saldoPendiente-=valor

# Menú principal
while True:
    print("Menú:")
    print("1. Registrar usuario")
    print("2. Iniciar sesión")
    print("3. Calcular cuotas de compra")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        if iniciar_sesion():
            print("Sesión iniciada.")
    elif opcion == "3":
        calcular_cuotas()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")