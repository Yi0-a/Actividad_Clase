inventario = {"huevos":12000, "carne":20000, "arroz":2000, "lenteja":1500, "leche": 4000, "Garbanzo":2000, "Cafe": 5000, "Azucar": 3000, "pollo": 10000}
print("Producto Precio")
def mostrar_inventario():
    for producto,precio in inventario.items():
        print(producto,precio)
mostrar_inventario()