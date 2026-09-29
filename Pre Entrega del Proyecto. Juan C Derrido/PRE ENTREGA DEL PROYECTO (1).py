# Lista para almacenar productos donde cada producto será una tupla (id, nombre, precio, categoria)
productos = []
 

while True:
    print("-" * 40)
    print("Menú Principal")
    print("-" * 40)
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Salir")
    print()

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        print("\n Agregar Productos: ")
        nombre = input("Nombre del producto: ")

        # Validar que el nombre no esté vacío
        if nombre.isdigit() or nombre.strip() == "":
            print("Nombre no válido!")
            continue

        # Solicitar el precio del producto, asegurándose de que sea un número válido
        while True:
            precio = input("Precio del producto: ")
            if precio.replace('.', '', 1).isdigit():
                precio = float(precio)
                break
            else:
                print("Precio no válido. Intente de nuevo.")

        categoria = input("Categoría del producto: ")

        id_actual = 1  # Contador para asignar un id único a cada producto

        nuevo_producto = (id_actual, nombre, precio, categoria)
        productos.append(nuevo_producto)
        print(f"Producto '{nombre}' agregado exitosamente.")
        id_actual += 1              # Incrementa el ID para el próximo producto

    elif opcion == '2':
        if not productos:
            print("No hay productos.")
        else:
            print("\n Inventario de productos:")
            for producto in productos:
                print(f"ID: {producto[0]}, Nombre: {producto[1]}, Precio: ${producto[2]}, Categoría: {producto[3]}")
    elif opcion == '3':
        print("Saliendo de la aplicación...")
        break
    else:
        print("Opción no válida, intente nuevamente.")

