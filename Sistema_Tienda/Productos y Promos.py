with open("Inventario.txt", "r") as archivo:
    inventario = archivo.readlines()

with open("Promociones.txt", "r") as archivo:
    promociones = archivo.readlines()


print("INVENTARIO:")
for producto in inventario:
    print(producto.strip())

print("\nPROMOCIONES:")
for promocion in promociones:
    print(promocion.strip())
    