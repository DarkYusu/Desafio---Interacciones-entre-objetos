from producto import Producto

class Tienda:
    def __init__(self, nombre, costo_delivery):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def costo_delivery(self):
        return self.__costo_delivery

    def ingresar_producto(self, producto):
        for p in self.__productos:
            if p.nombre == producto.nombre:
                p.actualizar_stock(producto.stock)
                return
        self.__productos.append(producto)

    def listar_productos(self):
        productos_str = []
        for producto in self.__productos:
            productos_str += str(producto) + "\n"
        return productos_str

    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self.__productos:
            if producto.nombre == nombre_producto:
                if cantidad <= producto.stock:
                    producto.actualizar_stock(-cantidad)
                    return True
                else:
                    print("Cantidad requerida superior al stock disponible.")
                    return False
        print("Producto no encontrado en la tienda.")
        return False

def crear_tienda():
    nombre = input("Ingrese el nombre de la tienda: ")
    costo_delivery = float(input("Ingrese el costo de delivery: "))
    tipo_tienda = input("Ingrese el tipo de tienda (Restaurante/Supermercado/Farmacia): ")
    if tipo_tienda.lower() == "restaurante":
        return Restaurante(nombre, costo_delivery)
    elif tipo_tienda.lower() == "supermercado":
        return Supermercado(nombre, costo_delivery)
    elif tipo_tienda.lower() == "farmacia":
        return Farmacia(nombre, costo_delivery)
    else:
        print("Tipo de tienda no válido.")
        return None
    
class Restaurante(Tienda):
    def listar_productos(self):
        pass
        # productos_str = ""
        # for producto in self._Tienda__productos:
        #     productos_str += f"Nombre: {producto.nombre}, Precio: ${producto.precio}\n"
        # return productos_str

class Supermercado(Tienda):
    def listar_productos(self):
        productos_str = ""
        for producto in self._Tienda__productos:
            if producto.stock < 10:
                productos_str += f"Nombre: {producto.nombre}, Precio: ${producto.precio}, Pocos productos disponibles: {producto.stock}\n"
            else:
                productos_str += f"Nombre: {producto.nombre}, Precio: ${producto.precio}, Stock: {producto.stock}\n"
        return productos_str

class Farmacia(Tienda):
    def listar_productos(self):
        pass
        # productos_str = ""
        # for producto in self._Tienda__productos:
        #     if producto.precio > 15000:
        #         productos_str += f"Nombre: {producto.nombre}, Precio: ${producto.precio}, Envío gratis al solicitar este producto\n"
        #     else:
        #         productos_str += f"Nombre: {producto.nombre}, Precio: ${producto.precio}\n"
        # return productos_str

    def realizar_venta(self, nombre_producto, cantidad):
        for producto in self._Tienda__productos:
            if producto.nombre == nombre_producto:
                if cantidad > 3:
                    return False
                elif cantidad > producto.stock:
                    cantidad_vendida = producto.stock
                    producto.actualizar_stock(-cantidad_vendida)
                    total_venta = cantidad_vendida * producto.precio
                    if total_venta > 15000:
                        print("Envío gratis.")
                    else:
                        print("No tiene envio gratis.")
                    return True
                else:
                    producto.actualizar_stock(-cantidad)
                    total_venta = cantidad * producto.precio
                    if total_venta > 15000:
                        print("Envío gratis.")
                    else:
                        print("No tiene envio gratis.")
                    return True
        return False