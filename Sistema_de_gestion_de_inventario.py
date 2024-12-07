# Sistema de gestion de inventario en Python

productos = []
ventas = []

# Esta funcion es para agregar un producto
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese el stock del producto: "))
    productos.append({"nombre": nombre, "precio": precio, "stock": stock})
    print("Producto agregado con éxito.\n")

# Verifica si un producto está disponible
def verificar_disponibilidad():
    nombre = input("Ingrese el nombre del producto que desea verificar: ")
    for producto in productos:
        if producto["nombre"] == nombre:
            print(f"El producto '{nombre}' está disponible con {producto['stock']} en stock.\n")
            return
    print(f"El producto '{nombre}' no está disponible.\n")

# En esta se realiza una venta
def realizar_venta():
    nombre = input("Ingrese el nombre del producto que desea comprar: ")
    cantidad = int(input("Ingrese la cantidad que desea comprar: "))
    
    for producto in productos:
        if producto["nombre"] == nombre:
            if producto["stock"] >= cantidad:
                producto["stock"] -= cantidad
                total = producto["precio"] * cantidad
                ventas.append({"nombre": nombre, "cantidad": cantidad, "total": total})
                print(f"Venta realizada con éxito. Total a pagar: ${total:.2f}\n")
            else:
                print("Stock insuficiente.\n")
            return
    print("Producto no encontrado.\n")

# Calcula el precio total de una compra
def calcular_precio_total():
    total = sum(venta["total"] for venta in ventas)
    print(f"El precio total de todas las ventas es: ${total:.2f}\n")

# Genera un informe con los productos más vendidos
def generar_informe():
    if not ventas:
        print("No se han realizado ventas.\n")
        return

    resumen = {}
    for venta in ventas:
        if venta["nombre"] in resumen:
            resumen[venta["nombre"]] += venta["cantidad"]
        else:
            resumen[venta["nombre"]] = venta["cantidad"]

    producto_mas_vendido = max(resumen, key=resumen.get)
    print(f"El producto más vendido es '{producto_mas_vendido}' con {resumen[producto_mas_vendido]} unidades vendidas.\n")

# Aqui mostramos los productos
def mostrar_productos():
    if productos:
        print("Productos disponibles:")
        for producto in productos:
            print(f"{producto['nombre']} - Precio: ${producto['precio']:.2f}, Stock: {producto['stock']}")
        print()
    else:
        print("No hay productos disponibles.\n")

# Menú principal
def menu():
    while True:
        print("=== Tienda en Línea ===")
        print("1. Agregar Producto")
        print("2. Verificar Disponibilidad")
        print("3. Realizar Venta")
        print("4. Calcular Precio Total de Ventas")
        print("5. Generar Informe de Productos Más Vendidos")
        print("6. Mostrar Productos")
        print("7. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            verificar_disponibilidad()
        elif opcion == "3":
            realizar_venta()
        elif opcion == "4":
            calcular_precio_total()
        elif opcion == "5":
            generar_informe()
        elif opcion == "6":
            mostrar_productos()
        elif opcion == "7":
            print("Gracias por usar el sistema. Adios")
            break
        else:
            print("Opción no válida.\n")

if __name__ == "__main__":
    menu()