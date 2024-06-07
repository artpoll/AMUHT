from PIL import Image, ImageTk 
from tkinter import Label
import tkinter as tk
from database import *
import os, sys 

conn, cursor = initialize_connection()

def center_window(width, height):
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

class WelcomeWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        logoIcon = Image.open(resource_path('Tamazula.png'))
        photo = ImageTk.PhotoImage(logoIcon)
        logo = Label(self, image=photo)
        logo.image = photo
        logo.place(x=50, y=80)
        self.master.iconbitmap(resource_path('artpoll.ico'))
        self.master.title("AMUHT")
        self.master.resizable(False, False)
        center_window(400, 300)     
        login_button = tk.Button(self, text="Entrar", font=35, width=10, height=3, bd=5, 
                                 cursor='hand2', background = "green", fg = "white", command=self.open_login_window)
        login_button.pack(padx=100, pady=25, side="top")
        register_button = tk.Button(self, text="Registrar", font=35, width=10, height=3, 
                                    bd=5, cursor='hand2', background = "green", fg = "white", command=self.open_register_window)
        register_button.pack(padx=15, pady=25, side="bottom")
        self.pack()

    def open_login_window(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        LoginWindow(self.master)
    def open_register_window(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        RegisterWindow(self.master)
class LoginWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Entrar")
        self.master.resizable(False, False)
        center_window(400, 300)         

        tk.Label(self, text="Usuario:", font=35).grid(row=1, column=0)
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=1, column=1, padx=10, pady=40)

        tk.Label(self, text="Contraseña:", font=35).grid(row=2, column=0)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=10)

        submit_button = tk.Button(self, text="Entrar", font=35, width=8, bd=5, cursor='hand2',  
                                  background = "green", fg = "white", command=self.submit)
        submit_button.grid(row=6, column=1, sticky="e", padx=10, pady=(50, 0))
        submit_button = tk.Button(self, text="Atras", font=35, width=8, bd=5, cursor='hand2', 
                                  background = "green", fg = "white", command=self.back)
        submit_button.grid(row=6, column=0, sticky="w", padx=10, pady=(50, 0))
        self.pack()
    def submit(self):
        data = {}
        data["email"] = self.username_entry.get()
        data["password"] = self.password_entry.get()
        if login(cursor, data) == True:
            print("successful login")
            for widget in self.winfo_children(): 
                widget.destroy()
            self.destroy()
            MainWindow(self.master)
        else:
            print("unsuccessful login")
    def back(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        WelcomeWindow(self.master)
class RegisterWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self.master.title("Registro")
        self.master.resizable(False, False)
        center_window(320, 370)
        tk.Label(self, text="Nombre: ").grid(row=0, column=0, sticky="w")
        self.first_name_entry = tk.Entry(self, width=26)
        self.first_name_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")
        tk.Label(self, text="Apellidos: ").grid(row=1, column=0, sticky="w")
        self.last_name_entry = tk.Entry(self, width=26)
        self.last_name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="e")
        tk.Label(self, text="Contraseña: ").grid(row=2, column=0, sticky="w")
        self.password_entry = tk.Entry(self, show="*", width=26)
        self.password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="e")
        tk.Label(self, text="Email: ").grid(row=3, column=0, sticky="w")
        self.email_entry = tk.Entry(self, width=26)
        self.email_entry.grid(row=3, column=1, padx=10, pady=10, sticky="e")
        tk.Label(self, text="Genero: ").grid(row=4, column=0, sticky="w")
        self.gender_entry = tk.Entry(self, width=10)
        self.gender_entry.grid(row=4, column=1, padx=10, pady=10, sticky="e")
        tk.Label(self, text="Edad: ").grid(row=5, column=0, sticky="w")
        self.age_entry = tk.Entry(self, width=10)
        self.age_entry.grid(row=5, column=1, padx=10, pady=10, sticky="e")
        tk.Label(self, text="Domicilio: ").grid(row=6, column=0, sticky="w")
        self.address_entry = tk.Text(self, width=20, height=3)
        self.address_entry.grid(row=6, column=1, padx=10, pady=10, sticky="e")
        submit_button = tk.Button(self, text="Enviar", width=8, bd=5, background = "green", 
                                  fg = "white",cursor='hand2', command=self.submit)
        submit_button.grid(row=7, column=1, padx=15, pady=15, sticky="e")
        submit_button = tk.Button(self, text="Atrás", width=8, bd=5, background = "green", 
                                  fg = "white", cursor='hand2', command=self.back)
        submit_button.grid(row=7, column=0, sticky="w", padx=15, pady=15)
        self.pack()
    def submit(self):
        data = {}
        data["firstName"] = self.first_name_entry.get()
        data["lastName"] = self.last_name_entry.get()
        data["password"] = self.password_entry.get()
        data["email"] = self.email_entry.get() 
        data["gender"] = self.gender_entry.get()
        data["age"] = self.age_entry.get()
        data["address"] = self.address_entry.get(1.0, tk.END)
        register(cursor, conn, data)
    def back(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        WelcomeWindow(self.master)
class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__()
        self.master = master
        logoIcon = Image.open(resource_path("Tamazula.png"))
        photo = ImageTk.PhotoImage(logoIcon)
        logo = Label(self, image=photo)
        logo.image = photo
        logo.place(x=20, y=80)
        self.master.title("Panel Principal")
        self.master.resizable(False, False)
        center_window(400, 350)
        submit_button = tk.Button(self, text="Secretaria General", font=35, background = "green", fg = "white", 
                                  width=15, bd=5, cursor='hand2', command=self.MSG)
        submit_button.grid(row=0, column=0, padx=15, pady=15, sticky="e")

        submit_button = tk.Button(self, text="Archivo Historico", font=35, background = "green", fg = "white", 
                                  width=13, bd=5, cursor='hand2', command=self.MAH)
        submit_button.grid(row=1, column=0, padx=15, pady=15, sticky="e")

        submit_button = tk.Button(self, text="Obras Publicas", font=35, background = "green", fg = "white", 
                                  width=13, bd=5, cursor='hand2', command=self.MOP)
        submit_button.grid(row=2, column=0, padx=15, pady=15, sticky="e")

        submit_button = tk.Button(self, text="Oficial Mayor", font=35, background = "green", fg = "white", 
                                  width=11, bd=5, cursor='hand2', command=self.MOM)
        submit_button.grid(row=3, column=0, padx=15, pady=15, sticky="e")

        submit_button = tk.Button(self, text="Registro Civil", font=35, background = "green", fg = "white", 
                                  width=11, bd=5, cursor='hand2', command=self.MRC)
        submit_button.grid(row=0, column=1, padx=15, pady=15, sticky="w")

        submit_button = tk.Button(self, text="Sindico Municipal", font=35, background = "green", fg = "white", 
                                  width=13, bd=5, cursor='hand2', command=self.MSM)
        submit_button.grid(row=1, column=1, padx=15, pady=15, sticky="w")

        submit_button = tk.Button(self, text="Tesoreria", font=35, background = "green", fg = "white", 
                                  width=8, bd=5, cursor='hand2', command=self.MT)
        submit_button.grid(row=2, column=1, padx=15, pady=15, sticky="w")

        submit_button = tk.Button(self, text="Catastro", font=35, background = "green", fg = "white", 
                                  width=8, bd=5, cursor='hand2', command=self.MC)
        submit_button.grid(row=3, column=1, padx=15, pady=15, sticky="w")

        submit_button = tk.Button(self, text="Atras", font=35, background = "grey", fg = "black", 
                                  width=8, bd=5, cursor='hand2', command=self.back)
        submit_button.grid(row=4, column=0, sticky="e", padx=15, pady=15)
        self.pack()

    def MSG(self):
        self.master.withdraw()
        path = ("C:/Modulos/MSG.exe")
        os.system(path)
        self.master.destroy()
    def MOM(self):
        self.master.withdraw()
        path = ("C:/Modulos/MOM.exe")
        os.system(path)
        self.master.destroy()
    def MT(self):
        self.master.withdraw()
        path = ("C:/Modulos/MT.exe")
        os.system(path)
        self.master.destroy()
    def MRC(self):
        self.master.withdraw()
        path = ("C:/Modulos/MRC.exe")
        os.system(path)
        self.master.destroy()    
    def MC(self):
        self.master.withdraw()
        path = ("C:/Modulos/MC.exe")
        os.system(path)
        self.master.destroy()
    def MOP(self):
        self.master.withdraw()
        path = ("C:/Modulos/MOP.exe")
        os.system(path)
        self.master.destroy()
    def MSM(self):
        self.master.withdraw()
        path = ("C:/Modulos/MSM.exe")
        os.system(path)
        self.master.destroy()
    def MAH(self):
        self.master.withdraw()
        path = ("C:/Modulos/MAH.exe")
        os.system(path)
        self.master.destroy()    

    def back(self):
        for widget in self.winfo_children(): 
            widget.destroy()
        self.destroy()
        WelcomeWindow(self.master)    
root = tk.Tk()
root.eval('tk::PlaceWindow . center')
WelcomeWindow(root)
root.mainloop()
