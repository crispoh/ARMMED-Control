import math
from tkinter import messagebox
import customtkinter
import os
from PIL import Image
import csv 
import datetime

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        ############ Obtener variables de inputs ############
        def obtenervariables():
            id = self.idEntry.get()
            nombre = self.nombreEntry.get()
            rut = self.rutEntry.get()
            grado = self.anguloEntry.get()
            tiempo_ciclo = self.ciclotEntry.get()
            tiempo_total = self.tiempoEntry.get()
            fecha= datetime.datetime.now()
            datos_usuario = [id, nombre, rut, grado, tiempo_ciclo, tiempo_total, fecha]
            ##Crear condicionales para que no se ingresen valores vacios o no numericos
            if int(grado) == 0 or int(tiempo_ciclo) == 0 or int(tiempo_total) == 0:
                print("No se puede ingresar cero")
                messagebox.showerror("Error", "Los valores no pueden esta vacios o ser 0" +"\n"+ "Por favor ingrese valores validos")
            if int(grado) > 90 and int(grado) < 0:
                print("El angulo no puede ser mayor a 90°")
                messagebox.showerror("Error", "El angulo no puede ser mayor a 90°")
            else:
                if int(tiempo_ciclo) > int(tiempo_total)*60:
                    print("El tiempo de ciclo no puede ser mayor al tiempo total")
                    messagebox.showerror("Error", "El tiempo de ciclo no puede ser mayor al tiempo total"+"\n"+ "Por favor ingrese valores validos")
                else: 
                    transformar_variables(grado, tiempo_ciclo, tiempo_total, datos_usuario)

        ############ Transformar variables ############
        def transformar_variables(grado, tiempo_ciclo, tiempo_total, datos_usuario):
            
            tiempoensegundos = int(tiempo_total) * 60
            numero_de_ciclos = int(tiempoensegundos)/int(tiempo_ciclo)
            ##aproximar a entero con .floor
            numero_de_ciclos = math.floor(numero_de_ciclos)
            medios_ciclos = int(numero_de_ciclos)*2

            print("El brazo se movera a un angulo de: " + str(grado) + "grados" +"\n"+ 
                  "Durante: "+ str(tiempoensegundos)+ "segundos" +"\n"+ 
                  "Una cantidad de: " + str(numero_de_ciclos) + "ciclos")

            messagebox.showinfo("Datos", "Se va a ejecutar el ejercicio con los siguientes datos:" + "\n" 
                                "Angulo de trabajo: "+ str(grado) + " grados" +"\n"
                                "Tiempo de ciclo: "+ str(tiempo_ciclo) + " segundos" +"\n"
                                "Numero de ciclos: "+ str(numero_de_ciclos) + " ciclos" +"\n"
                                "Tiempo total en segundos: "+ str(tiempoensegundos) + " segundos")
            
            ##Confirmar datos por el usuario con un messagebox de aceptar o cancelar    
            if messagebox.askokcancel("Confirmar", "¿Desea continuar con el Ejercicio?"):
                ##Iniciar ejercicio
                ingresar_usuario(datos_usuario)
                ##Ciclos, tiempo ciclo, tiempo total
                iniciar_ejercicio(grado, numero_de_ciclos, tiempo_ciclo, tiempoensegundos)
                ##Ejercicio terminado
                print("Ejercicio terminado")
                messagebox.showinfo("Terminado", "Ejercicio terminado")
            else:
                print("Ejercicio cancelado")
                messagebox.showinfo("Cancelado", "Ejercicio cancelado")

        ############ Creacion del .csv de pacientes e ingreso de datos ############
        def ingresar_usuario(datos_usuario):
            archivo_csv = 'pacientes.csv'
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
                        # Escribir una nueva fila con los datos
                        escritor_csv.writerow(datos_usuario)
                        print("Datos ingresados correctamente")
        
        ############ Iniciar ejercicio ############
        def iniciar_ejercicio(grados, ciclos, tiempo_ciclo, tiempo_total):
            print("Iniciar ejercicio")
            print("Enviando datos a Arduino")
            ##Concatnar datos para enviar a arduino separados por comas
            datos = str(grados) + "," + str(ciclos) + "," + str(tiempo_ciclo) + "," + str(tiempo_total)
            ##Enviar datos a arduino
            ##arduino.write(datos.encode())
            print("Datos enviados:" + datos)
            print("Ejercicio iniciado")

        ############ Crear ventana ############
        self.title("ARMMED - Cotrol")
        self.geometry("850x650")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        ############### Cargar imagenes ################
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "config_image_light.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "config_image_dark.png")), size=(550, 550))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "play_icon_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "play_icon_light.png")), size=(15, 15))

        ############### Navigation Frame ################

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  ARMMED - Control", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=0, border_spacing=10, text="Configuración",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        ############### Frame Variables paciente ################
        self.frameuser = customtkinter.CTkFrame(self.navigation_frame, width=70)
        self.frameuser.grid(column=0, row=2, padx=5,pady=5)
        
        #### Label ID Paciente
        self.idLabel = customtkinter.CTkLabel(self.frameuser, text="ID Paciente")
        self.idLabel.grid(row=0, column=0, padx=20, pady=(10,3), sticky="ew")
        #### Entry Nombre Paciente ## DATO A INGRESAR
        self.idEntry = customtkinter.CTkEntry(self.frameuser, placeholder_text="Ingresar", justify="center")
        self.idEntry.grid(row=1, column=0, padx=20, pady=(3,5), sticky="ew", )
        #### Label RUT Paciente
        self.nombreLabel = customtkinter.CTkLabel(self.frameuser, text="Nombre Paciente")
        self.nombreLabel.grid(row=2, column=0, padx=20, pady=(5,3), sticky="ew")
        #### Entry RUT Paciente ## DATO A INGRESAR
        self.nombreEntry = customtkinter.CTkEntry(self.frameuser, placeholder_text="Ingresar", justify="center")
        self.nombreEntry.grid(row=3, column=0, padx=20, pady=(3,5), sticky="ew", )

        #### Label RUT Paciente
        self.rutLabel = customtkinter.CTkLabel(self.frameuser, text="RUT Paciente")
        self.rutLabel.grid(row=4, column=0, padx=20, pady=(5,3), sticky="ew")
        #### Entry RUT Paciente ## DATO A INGRESAR
        self.rutEntry = customtkinter.CTkEntry(self.frameuser, placeholder_text="Ej: 12.345.678-k", justify="center")
        self.rutEntry.grid(row=5, column=0, padx=20, pady=(3,10), sticky="ew", )

        ############### Fin Frame Variables pacientes ################

        ############### Frame Variables ################
        self.frame1 = customtkinter.CTkFrame(self.navigation_frame, width=70)
        self.frame1.grid(column=0, row=3, padx=5,pady=5)

        #### Label Angulo Brazo
        self.anguloLabel = customtkinter.CTkLabel(self.frame1, text="Angulo Brazo (°)")
        self.anguloLabel.grid(row=0, column=0, padx=20, pady=(10,3), sticky="ew")
        #### Entry Angulo Brazo ## DATO A INGRESAR
        self.anguloEntry = customtkinter.CTkEntry(self.frame1, placeholder_text="Ingresar", justify="center")
        self.anguloEntry.grid(row=1, column=0, padx=20, pady=(3,5), sticky="ew", )

        #### Label Velocidad
        self.ciclotLabel = customtkinter.CTkLabel(self.frame1, text="Tiempo Ciclo (seg)")
        self.ciclotLabel.grid(row=2, column=0, padx=20, pady=(5,3), sticky="ew")
        #### Entry Velocidad ## DATO A INGRESAR
        self.ciclotEntry = customtkinter.CTkEntry(self.frame1, placeholder_text="Ingresar", justify="center")
        self.ciclotEntry.grid(row=3, column=0, padx=20, pady=(3,5), sticky="ew", )

        #### Label Tiempo
        self.tiempoLabel = customtkinter.CTkLabel(self.frame1, text="Tiempo Tratamiento (min)")
        self.tiempoLabel.grid(row=4, column=0, padx=20, pady=(5,3), sticky="ew")
        #### Entry Tiempo ## DATO A INGRESAR
        self.tiempoEntry = customtkinter.CTkEntry(self.frame1, placeholder_text="Ingresar", justify="center")
        self.tiempoEntry.grid(row=5, column=0, padx=20, pady=(3,15), sticky="ew", )

        ##boton iniciar
        self.iniciar_ejercicio = customtkinter.CTkButton(self.frame1, text="Iniciar Ejercicio", image=self.chat_image, compound="right", command=obtenervariables)
        self.iniciar_ejercicio.grid(row=6, column=0, padx=20, pady=(0,15))

        ############### Fin Frame Variables ################

        

        

        ##seleccionar modo ventana
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["System","Light", "Dark"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=(20,0), sticky="s")

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="by CrisPoh", font=customtkinter.CTkFont(size=10))
        self.navigation_frame_label.grid(row=7)

        ############### Fin Navigation Frame ################


        # Crea el home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=20)

        # Selecciona el frame home como el frame inicial a mostrar
        self.select_frame_by_name("home")

    def select_frame_by_name(self, name):
        # set button color for selected button
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")

        # show selected frame
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()

    def home_button_event(self):
        self.select_frame_by_name("home")


    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)


if __name__ == "__main__":
    app = App()
    app.mainloop()

