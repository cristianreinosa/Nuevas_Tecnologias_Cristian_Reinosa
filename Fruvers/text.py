from Frute import Frute

frute = Frute(id=None,
              nombre=None,
              tipo=None,
              cantidad=None,
              precio=None)



def menuApp():
    print("Inicie con 1")

    init = int(input("Escriba 1"))

    while init != 0:
        print("Seleccione 1 para registrar producto\n"
              "Seleccione 2 para imprimir registro \n"
              "Seleccione 3 para calcular precio\n"
              "Selelccione 4 para salir")

        opc = int(input("Ingrese una opcion"))

        if opc == 1:
            frute.registrar_produc()
        elif opc == 2:
            frute.imprimir_registro()
        elif opc == 3:
            resultado = frute.calculo_precio()
            print("Total a pagar es:",resultado)
        elif opc == 4:
            print("Salir")


menuApp()
