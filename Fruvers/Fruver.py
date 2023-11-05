class Fruver:
    def __init__(self, id, nombre, tipo):
        self._id = id
        self._nombre = nombre
        self._tipo = tipo

    @property
    def id(self):
        return self._id
    @id.setter
    def id(self,id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def id(self, nombre):
        self._nombre = nombre

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def id(self, tipo):
        self._tipo = tipo


    def registro_producto(self):
        id = input("Ingrese el Id del producto")
        nombre = input("Ingrese el nombre del producto")
        tipo = input("Ingrese el tipo del producto")

    def imprimir_producto(self):
        print(f"Id: {self._id}, Nombre: {self._nombre}, Tipo: {self._tipo}")