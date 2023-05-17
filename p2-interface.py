import math
from tkinter import messagebox
import customtkinter
import os
from PIL import Image


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        def obtenervariables():
            grado = self.anguloEntry.get()
            tiempo_ciclo = self.ciclotEntry.get()
            tiempo_total = self.tiempoEntry.get()
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
                    incicio_de_ejercicio(grado, tiempo_ciclo, tiempo_total)

        def incicio_de_ejercicio(grado, tiempo_ciclo, tiempo_total):
            
            tiempoensegundos = int(tiempo_total) * 60
            numero_de_ciclos = int(tiempoensegundos)/int(tiempo_ciclo)
            ##aproximar a entero con .floor
            numero_de_ciclos = math.floor(numero_de_ciclos)
            medios_ciclos = int(numero_de_ciclos)*2

            print("El brazo se movera a un angulo de: " + str(grado) + "grados" +"\n"+ 
                  "Durante: "+ str(tiempoensegundos)+ "segundos" +"\n"+ 
                  "Una cantidad de: " + str(numero_de_ciclos) + "ciclos")
            ##for i in range(numero_de_ciclos):

        


        self.title("ARMMED - Cotrol")
        self.geometry("780x540")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # load images with light and dark mode image
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_images")
        self.logo_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "CustomTkinter_logo_single.png")), size=(26, 26))
        self.large_test_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "setup.png")), size=(500, 500))
        self.image_icon_image = customtkinter.CTkImage(Image.open(os.path.join(image_path, "image_icon_light.png")), size=(20, 20))
        self.home_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "home_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "home_light.png")), size=(20, 20))
        self.chat_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "chat_dark.png")),
                                                 dark_image=Image.open(os.path.join(image_path, "chat_light.png")), size=(15, 15))
        self.add_user_image = customtkinter.CTkImage(light_image=Image.open(os.path.join(image_path, "add_user_dark.png")),
                                                     dark_image=Image.open(os.path.join(image_path, "add_user_light.png")), size=(20, 20))

        ############### Navigation Frame ################

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(4, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="  ARMMED - Control", image=self.logo_image,
                                                             compound="left", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.home_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Configuración",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")

        ############### Frame Variables ################
        self.frame1 = customtkinter.CTkFrame(self.navigation_frame, width=70)
        self.frame1.grid(column=0, row=2, padx=5,pady=10)

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

        ############### Fin Frame Variables ################

        ##boton iniciar
        self.iniciar_ejercicio = customtkinter.CTkButton(self.navigation_frame, text="Iniciar Ejercicio", image=self.chat_image, compound="right", command=obtenervariables)
        self.iniciar_ejercicio.grid(row=3, column=0, padx=20, pady=0)

        ##seleccionar modo ventana
        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=6, column=0, padx=20, pady=(20,0), sticky="s")

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="by CrisPoh", font=customtkinter.CTkFont(size=10))
        self.navigation_frame_label.grid(row=7)

        ############### Fin Navigation Frame ################


        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.large_test_image)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=20)

        # select default frame
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

