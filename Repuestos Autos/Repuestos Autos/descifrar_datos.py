from cryptography.fernet import Fernet
import mysql.connector
import os

# -----------------------------
# Funciones de carga y descifrado
# -----------------------------
def cargar_clave():
    with open("clave.key", "rb") as archivo:
        return archivo.read()

def descifrar(valor_cifrado):
    f = Fernet(cargar_clave())
    return f.decrypt(valor_cifrado.encode()).decode()

# -----------------------------
# Función para descifrar los campos específicos en MySQL
# (stock, precio_fabrica, codigo_barras)
# -----------------------------
def descifrar_campos_especificos():
    conexion = mysql.connector.connect(
        host="host.docker.internal",
        user="root",
        password="santi654",
        database="taller_repuestos"
    )
    cursor = conexion.cursor()

    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    columnas = [desc[0] for desc in cursor.description]

    for producto in productos:
        id_producto = producto[0]
        actualizaciones = {}

        for i, columna in enumerate(columnas):
            valor = producto[i]
            if columna == 'stock' and valor is not None:
                try:
                    actualizaciones['stock'] = descifrar(valor)
                except Exception as e:
                    print(f"Error al descifrar el campo 'stock' para el ID {id_producto}: {e}")
            elif columna == 'precio_fabrica' and valor is not None:
                try:
                    actualizaciones['precio_fabrica'] = descifrar(valor)
                except Exception as e:
                    print(f"Error al descifrar el campo 'precio_fabrica' para el ID {id_producto}: {e}")
            elif columna == 'codigo_barras' and valor is not None:
                try:
                    actualizaciones['codigo_barras'] = descifrar(valor)
                except Exception as e:
                    print(f"Error al descifrar el campo 'codigo_barras' para el ID {id_producto}: {e}")

        if actualizaciones:
            set_clause = ", ".join([f"{col} = %s" for col in actualizaciones])
            valores = list(actualizaciones.values())
            valores.append(id_producto)
            consulta = f"UPDATE productos SET {set_clause} WHERE id_producto = %s"
            cursor.execute(consulta, valores)

    conexion.commit()
    cursor.close()
    conexion.close()
    print("Descifrado de stock, precio_fabrica y codigo_barras completado.")

# -----------------------------
# Ejecutar el descifrado 
# -----------------------------
if __name__ == "__main__":
    generar_clave()
    cifrar_campos_especificos() 

