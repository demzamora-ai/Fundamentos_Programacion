productos = {
"Mouse": [10, 15000],
"Teclado": [5, 25000],
"Monitor": [3, 180000]
}

#definicion de funciones
def agregar_producto(productos):
    nombre = input ("Nombre del producto: ").strip()

    if nombre.isdigit():
     print("Debe ingresar letras!!!")


    if nombre =="":
        print("El nombre no puede ser vacio")
        return
    if nombre in productos:
        print("El producto ya existe!")
        return 
    while (True): 
        try: 
            stock = int(input("Ingrese stock: "))
            
        except:
            print("Debe ingresar un numero!!, vuelva a intentar")

        while (True):
            try:
                precio = int(input("Ingrese precio"))
                break
            except:
                print("Debe ingresar un numero!!, vuelve a intentar ")

        productos[nombre] = [stock, precio]
        print("Productos agregados correctamente!")


def mostrar_productos(productos):
    if len(productos) == 0:
        print("No existen productos")
        return
for nombre in productos:
    print(nombre,"--stock:",productos[nombre][0],"--Precio:",productos[nombre][0])


    def buscar_producto(productos):
        if len (productos) == 0 :
            print("No existen productos")
            return
        
        nombre = input("Nombre producto a buscar: ").strip()

        if nombre in productos:
            print("Producto encontrado")
            print(f"Stock:{productos[nombre][0]}")
            print(f"precio $ {productos[nombre][1]}")
        else:
           print("Producto no existe o agotado")
def producto_mas_caro(productos):
    if len(productos) == 0 :
        print("No existen productos")
        return
    mayor = 0
    mayor_Nombre = ""
    for nombre in productos :
      precio = productos[nombre][1]
       
      if precio > mayor :
          mayor_nombre=nombre

    print(f"Producto mas caro es {mayor_nombre}")
    print(f"")

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

