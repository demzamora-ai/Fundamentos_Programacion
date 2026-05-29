productos = {
"Mouse": [10, 15000],
"Teclado": [5, 25000],
"Monitor": [3, 180000]
}


#definicion de funciones
def agregar_producto(productos):
    nombre = input ("Nombre del producto: ").strip()

    if nombre =="":
        print("El nombre no puede ser vacio")
        return
    if nombre in productos:
        print("El producto ya existe!")
        return 
    stock = int(input("Ingrese stock: "))
    precio = int(input("Ingrese precio"))
    productos[nombre] = [stock, precio]
    print("Productos agregados correctamente!")



productos={}

while (True):
    print("---MENU---")
    print("1.Agregar producto")
    print("2.Mostrar productos")
    print("3.Buscar productos")
    print("4.Producto mas caro")
    print("5.Salir")

    while (True):
        try:
            op = int(input("Seleccione opcion"))
            break
        except ValueError:
            print("Error, debe ingresar un numero entre 1 y 5, Intente nuevamente")

    if op == 1:
        agregar_producto(productos)
    elif op == 2:
        print("2")
    # mostrar_productos(productos)
    elif op == 3:
        #buscar_producto(producto)
        print("3")
    elif op == 4:
        #producto_mas_caro(producto)
        print("4")
    elif op == 5 :
        print("Fin del programa")
    else:
        print("Opcion invalida")
