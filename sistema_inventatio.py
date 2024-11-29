# Inicializamos la lista de inventario
inventario = []

def agregar_producto(nombre, cantidad):
    """Agrega un producto al inventario."""
    inventario.append({"nombre": nombre, "cantidad": cantidad})

def mostrar_inventario():
    """Muestra todos los productos en el inventario."""
    if not inventario:
        print("El inventario está vacío.")
    else:
        print("Inventario:")
        for producto in inventario:
            print(f"Producto: {producto['nombre']}, Cantidad: {producto['cantidad']}")

# Menú interactivo
while True:
    print("\nMenú de Gestión de Productos:")
    print("1. Agregar productos al inventario")
    print("2. Mostrar productos registrados")
    print("3. Salir")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        nombre = input("Ingresa el nombre del producto: ")
        cantidad = int(input("Ingresa la cantidad del producto: "))
        agregar_producto(nombre, cantidad)
        print(f"Producto '{nombre}' agregado con cantidad {cantidad}.")
    elif opcion == "2":
        mostrar_inventario()
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")