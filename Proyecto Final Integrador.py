import sqlite3


# Crear y conectar la base de datos SQLite
def crear_bdd():
    conexion = sqlite3.connect("inventario.db")  
    cursor = conexion.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT NOT NULL
        )"""
    )
    conexion.commit()
    return conexion

conexion = crear_bdd()

def registrar_productos():
    try:
        nombre = input("Ingrese el nombre del producto: ")
        descripcion = input("Ingrese la descripción del producto: ")
        cantidad = int(input("Ingrese la cantidad disponible: "))
        precio = float(input("Ingrese el precio del producto: "))
        categoria = input("Ingrese la categoría del producto: ")
        
        cursor = conexion.cursor()
        cursor.execute('''INSERT INTO productos (nombre, descripcion, cantidad, precio, categoria)
                          VALUES (?, ?, ?, ?, ?)''', (nombre, descripcion, cantidad, precio, categoria))
        conexion.commit()
        print("Producto agregado exitosamente.")
    except Exception as e:
        print(f"Error al registrar producto: {e}")

def mostrar_productos():
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos")
        productos = cursor.fetchall()
        if productos:
            print(f"{'ID':<5} {'Nombre':<20} {'Cantidad':<10} {'Precio':<10} {'Categoría':<15}")
            print("-" * 60)
            for producto in productos:
                print(f"{producto[0]:<5} {producto[1]:<20} {producto[3]:<10} {producto[4]:<10} {producto[5]:<15}")
        else:
            print("No hay productos en el inventario.")
    except Exception as e:
        print(f"Error al mostrar productos: {e}")

def actualizar_productos():
    try:
        mostrar_productos()
        id_producto = int(input("Ingrese el ID del producto a actualizar: "))
        campo = input("Ingrese la columna a actualizar (nombre, descripcion, cantidad, precio, categoria): ")
        nuevo_valor = input("Ingrese el nuevo valor: ")
        
        cursor = conexion.cursor()
        query = f"UPDATE productos SET {campo} = ? WHERE id = ?"
        cursor.execute(query, (nuevo_valor, id_producto))
        conexion.commit()
        print("Producto actualizado exitosamente.")
    except Exception as e:
        print(f"Error al actualizar producto: {e}")

def eliminar_productos():
    try:
        mostrar_productos()
        id_producto = int(input("ID del producto a eliminar: "))
        
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM productos WHERE id = ?", (id_producto,))
        conexion.commit()
        print("Producto eliminado exitosamente.")
    except Exception as e:
        print(f"Error al eliminar producto: {e}")

def buscar_productos():
    try:
        criterio = input("Ingrese el nombre o categoría del producto a buscar: ")
        
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE nombre LIKE ? OR categoria LIKE ?", (f"%{criterio}%", f"%{criterio}%"))
        productos = cursor.fetchall()
        if productos:
            print(f"{'ID':<5} {'Nombre':<20} {'Cantidad':<10} {'Precio':<10} {'Categoría':<15}")
            print("-" * 60)
            for producto in productos:
                print(f"{producto[0]:<5} {producto[1]:<20} {producto[3]:<10} {producto[4]:<10} {producto[5]:<15}")
        else:
            print("No se encontraron productos.")
    except Exception as e:
        print(f"Error al buscar productos: {e}")

def reporte_bajo_stock():
    try:
        bajo_stock_de_producto = int(input("Ingrese el número que represente bajo stock: "))
        
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM productos WHERE cantidad <= ?", (bajo_stock_de_producto,))
        productos = cursor.fetchall()
        if productos:
            print(f"{'ID':<5} {'Nombre':<20} {'Cantidad':<10} {'Precio':<10} {'Categoría':<15}")
            print("-" * 60)
            for producto in productos:
                print(f"{producto[0]:<5} {producto[1]:<20} {producto[3]:<10} {producto[4]:<10} {producto[5]:<15}")
        else:
            print("No hay productos con bajo stock.")
    except Exception as e:
        print(f"Error al generar reporte de bajo stock: {e}")

def menu():
    while True:
        print("\n--- Menú del Inventario ---")
        print("1. Registrar producto")
        print("2. Mostrar productos")
        print("3. Actualizar producto")
        print("4. Eliminar producto")
        print("5. Reporte de bajo stock")
        print("6. Buscar producto")
        print("7. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_productos()
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            actualizar_productos()
        elif opcion == "4":
            eliminar_productos()
        elif opcion == "5":
            reporte_bajo_stock()
        elif opcion == "6":
            buscar_productos()
        elif opcion == "7":
            print("Saliendo de la aplicación...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

menu()
conexion.close()