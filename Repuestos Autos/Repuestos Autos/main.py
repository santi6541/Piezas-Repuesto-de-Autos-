from cifrado_productos import cifrar_campos_especificos, generar_clave
from descifrar_datos import descifrar_campos_especificos

def menu():
    while True:
        print("\n========== MENÚ ==========")
        print("1. Cifrar datos (stock, precio_fabrica, codigo_barras)")
        print("2. Descifrar datos")
        print("3. Salir")
        print("==========================")
        opcion = input("Seleccione una opción (1/2/3): ")

        if opcion == "1":
            generar_clave()
            cifrar_campos_especificos()
        elif opcion == "2":
            descifrar_campos_especificos()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
