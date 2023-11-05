from Fruver import Fruver

class Frute(Fruver):

    def __init__(self, id, nombre,tipo, cantidad, precio):
        super().__init__(id, nombre, tipo)
        self._cantidad = cantidad
        self._precio = precio

    @property
    def cantidad(self):
        return self._cantidad
    @cantidad.setter
    def cantidad(self,cantidad):
        self._cantidad = cantidad

    @property
    def precio(self):
        return self._precio
    @precio.setter
    def precio(self,precio):
        self._precio = precio

    def registrar_produc(self):
        self._id = input("Ingrese el Id del producto")
        self._nombre = input("Ingrese el nombre del producto")
        self._tipo = input("Ingrese el tipo del producto")
        self._cantidad = int(input("Ingrese la cantidad del producto"))
        self._precio = float(input("Ingrese el precio del producto"))

    def imprimir_registro(self):
        super().imprimir_producto()
        print(f"Cantidad: {self._cantidad} Precio: {self._precio}")

    def calculo_precio(self):
        print("Si la cantidad de productos son mayor de 7 productos y Si el precio es mayor a $1500 tiene el 50% de descuento")
        cantidad_produc = int(input("Ingrese la cantidad de productos"))
        precio_produc = float(input("Ingrese el precio del producto"))

        totalsin_descuento = cantidad_produc * precio_produc

        if cantidad_produc > 7 and precio_produc >= 1500:
            descuento = totalsin_descuento * 0.5
            total = totalsin_descuento - descuento
            print("Total sin descuento:", totalsin_descuento)
            print("Total con descuento (50%):", total)
        else:
            total = totalsin_descuento
            print("Total sin descuento:", total)

        return total





