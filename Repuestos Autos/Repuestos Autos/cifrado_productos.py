from cryptography.fernet import Fernet
import mysql.connector
import os

# -----------------------------
# 1. Generar clave (si no existe)
# -----------------------------
def generar_clave():
    if not os.path.exists("clave.key"):
        clave = Fernet.generate_key()
        with open("clave.key", "wb") as archivo:
            archivo.write(clave)

# -----------------------------
# 2. Funciones de cifrado y descifrado
# -----------------------------
def cargar_clave():
    with open("clave.key", "rb") as archivo:
        return archivo.read()

def cifrar(valor):
    f = Fernet(cargar_clave())
    return f.encrypt(str(valor).encode()).decode()

# -----------------------------
# 3. Función para cifrar 
# (stock, precio_fabrica, codigo_barras)
# -----------------------------
def cifrar_campos_especificos():
    conexion = mysql.connector.connect(
        host="host.docker.internal",
        user="root",
        password="santi654",
        database="taller_repuestos"
    )
    cursor = conexion.cursor()

    cursor.execute("SELECT id_producto, stock, precio_fabrica, codigo_barras FROM productos")
    productos = cursor.fetchall()

    for producto in productos:
        id_producto = producto[0]
        stock = producto[1]
        precio_fabrica = producto[2]
        codigo_barras = producto[3]

        actualizaciones = {}

        if stock is not None:
            actualizaciones['stock'] = cifrar(stock)
        if precio_fabrica is not None:
            actualizaciones['precio_fabrica'] = cifrar(precio_fabrica)
        if codigo_barras is not None:
            actualizaciones['codigo_barras'] = cifrar(codigo_barras)

        if actualizaciones:
            set_clause = ", ".join([f"{col} = %s" for col in actualizaciones])
            valores = list(actualizaciones.values())
            valores.append(id_producto)
            consulta = f"UPDATE productos SET {set_clause} WHERE id_producto = %s"
            cursor.execute(consulta, valores)

    conexion.commit()
    cursor.close()
    conexion.close()
    print("Cifrado de stock, precio_fabrica y codigo_barras completado.")

# -----------------------------
# 4. Ejecutar el cifrado 
# -----------------------------
if __name__ == "__main__":
    generar_clave()
    cifrar_campos_especificos()

