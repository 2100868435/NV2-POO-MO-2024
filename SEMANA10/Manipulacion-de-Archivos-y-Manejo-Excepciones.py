import os


class Producto:
    def __init__(self, codigo, nombre, cantidad, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def __str__(self):
        return f"{self.codigo},{self.nombre},{self.cantidad},{self.precio:.2f}"


class Inventario:
    def __init__(self, archivo):
        self.archivo = archivo
        self.productos = {}
        self.cargar_inventario()

    def cargar_inventario(self):
        if not os.path.exists(self.archivo):
            print(f"El archivo {self.archivo} no existe. Creando uno nuevo.")
            return

        try:
            with open(self.archivo, 'r') as file:
                for linea in file:
                    codigo, nombre, cantidad, precio = linea.strip().split(',')
                    self.productos[codigo] = Producto(codigo, nombre, int(cantidad), float(precio))
        except IOError as e:
            print(f"Error al leer el archivo: {e}")
        except ValueError as e:
            print(f"Error en el formato de los datos del archivo: {e}")

    def guardar_inventario(self):
        try:
            with open(self.archivo, 'w') as file:
                for producto in self.productos.values():
                    file.write(str(producto) + '\n')
            print("Inventario guardado exitosamente.")
        except IOError as e:
            print(f"Error al escribir en el archivo: {e}")

    def agregar_producto(self, producto):
        if producto.codigo in self.productos:
            raise Exception(f"El producto con código {producto.codigo} ya existe.")
        self.productos[producto.codigo] = producto
        print(f"Producto {producto.nombre} agregado al inventario.")
        self.guardar_inventario()

    def eliminar_producto(self, codigo):
        try:
            producto = self.productos.pop(codigo)
            print(f"Producto {producto.nombre} eliminado del inventario.")
            self.guardar_inventario()
        except KeyError:
            print(f"Error: No se encontró ningún producto con el código {codigo}.")

    def mostrar_inventario(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)


if __name__ == "__main__":
    inventario = Inventario('inventario.txt')

    while True:
        print("\nSistema de Gestión de Inventarios")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Mostrar inventario")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            codigo = input("Ingrese el código del producto: ")
            nombre = input("Ingrese el nombre del producto: ")
            cantidad = int(input("Ingrese la cantidad del producto: "))
            precio = float(input("Ingrese el precio del producto: "))
            try:
                producto = Producto(codigo, nombre, cantidad, precio)
                inventario.agregar_producto(producto)
            except Exception as e:
                print(e)
        elif opcion == '2':
            codigo = input("Ingrese el código del producto a eliminar: ")
            inventario.eliminar_producto(codigo)
        elif opcion == '3':
            inventario.mostrar_inventario()
        elif opcion == '4':
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")





