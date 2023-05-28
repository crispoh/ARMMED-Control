import csv
import os

def ingresar_usuario(datos_usuario, archivo_csv):
    # Verificar si el archivo CSV existe
    existe_archivo = os.path.isfile(archivo_csv)

    # Si el archivo no existe, crear uno nuevo y escribir las columnas
    if not existe_archivo:
        # Nombres de las columnas
        columnas = ['ID', 'Nombre', 'Rut', 'Angulo Trabajado', 'Tiempo Ciclo', 'Tiempo Tratamiento', 'Fecha']
        # Crear el archivo CSV y escribir los nombres de las columnas
        with open(archivo_csv, 'w', newline='') as archivo_csv:
            escritor_csv = csv.writer(archivo_csv)
            escritor_csv.writerow(columnas)
            escritor_csv.writerow(datos_usuario)
            print("Datos ingresados correctamente")
    else:
        with open(archivo_csv, 'a', newline='') as archivo_csv:
                # Crear un objeto escritor CSV
                escritor_csv = csv.writer(archivo_csv)
                # Escribir una nueva fila con los datos de "x", "y" y "Datos"
                escritor_csv.writerow(datos_usuario)
                print("Datos ingresados correctamente")
       
# Ejemplo de uso
datos_usuario = ['234', 'Joe Andres', '12.345.678-k', '10','5','20', '05-28-2023' ]
archivo_csv = 'usuarios.csv'

ingresar_usuario(datos_usuario, archivo_csv)
