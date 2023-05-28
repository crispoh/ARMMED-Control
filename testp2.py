import csv
import os

def ingresar_usuario(datos_usuario, archivo_csv):
    # Verificar si el archivo CSV existe
    existe_archivo = os.path.isfile(archivo_csv)

    # Si el archivo no existe, crear uno nuevo y escribir las columnas
    if not existe_archivo:
        with open(archivo_csv, 'w', newline='') as archivo:
            escritor_csv = csv.writer(archivo)
            escritor_csv.writerow(['ID', 'Nombre', 'Edad', 'Email'])  # Agregar la columna del ID

    # Abrir el archivo en modo de lectura para leer los registros anteriores (si existen)
    with open(archivo_csv, 'r', newline='') as archivo:
        lector_csv = csv.reader(archivo)
        registros_anteriores = list(lector_csv)

    # Determinar el siguiente ID disponible
    if existe_archivo:
        # Si el archivo ya existe, obtener el último ID y calcular el siguiente
        ultimo_id = int(registros_anteriores[-1][0])
        siguiente_id = ultimo_id + 1
    else:
        # Si el archivo no existe, establecer el primer ID como 1
        siguiente_id = 1

    # Crear la lista completa de datos del usuario con el ID
    datos_completos = [siguiente_id] + datos_usuario

    # Abrir el archivo en modo de escritura para agregar un nuevo registro en la última fila
    with open(archivo_csv, 'a', newline='') as archivo:
        escritor_csv = csv.writer(archivo)
        
        if existe_archivo:
            # Si el archivo ya existe, escribir los registros anteriores nuevamente
            for registro in registros_anteriores:
                escritor_csv.writerow(registro)

        # Escribir el nuevo registro en la última fila
        escritor_csv.writerow(datos_completos)

# Ejemplo de uso
datos_usuario = ['John Doe', '30', 'johndoe@example.com']
archivo_csv = 'usuarios.csv'

ingresar_usuario(datos_usuario, archivo_csv)
