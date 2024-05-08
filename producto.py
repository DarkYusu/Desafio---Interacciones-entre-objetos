class Producto:
    def __init__(self, nombre, precio, stock=0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    def actualizar_stock(self, cantidad):
        if cantidad < 0:
            if abs(cantidad) > self.__stock:
                self.__stock = 0
            else:
                self.__stock += cantidad
        else:
            self.__stock += cantidad

    def __str__(self):
        return f"Nombre: {self.__nombre}, Precio: ${int(self.__precio)}, Stock: {self.__stock}"