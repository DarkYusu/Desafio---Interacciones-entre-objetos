from tienda import Restaurante, Supermercado, Farmacia, crear_tienda
from producto import Producto

def crear_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = int(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto: "))
    return Producto(nombre, precio, stock)

def main():
    tienda = crear_tienda()
    if tienda is None:
        return

    while True:
        print("\nSeleccione una opción:")
        print("1. Ingresar producto")
        print("2. Listar productos")
        print("3. Realizar venta")
        print("4. Salir")
        print("")

        opcion = input("Opción: ")
        if opcion == "1":
            producto = crear_producto()
            tienda.ingresar_producto(producto)
            print("")
            print("Producto ingresado correctamente.")
        elif opcion == "2":
            print("")
            print("Productos existentes:")
            if isinstance(tienda, Supermercado):
                print(tienda.listar_productos())
            elif isinstance(tienda, Restaurante) or isinstance(tienda, Farmacia):
                print(tienda.listar_productos())
            else:
                print("Tipo de tienda no válido.")
        elif opcion == "3":
            nombre_producto = input("Ingrese el nombre del producto a vender: ")
            cantidad = int(input("Ingrese la cantidad a vender: "))
            if tienda.realizar_venta(nombre_producto, cantidad):
                print("Venta realizada con éxito.")
            else:
                print("No se pudo realizar la venta.")
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
