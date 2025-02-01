# punto 2

import math
from tkinter import *
from tkinter import messagebox

class Figuras:
    def __init__(self, figura):
        self.figura = figura

    def volumen(self):
        pass

    def superficie(self):
        pass

class Cilindro(Figuras):
    def __init__(self,radio,altura):
        self.radio = radio
        self.altura = altura
    def VolCil(self):
        VolumenC = math.pi * math.pow(self.radio,2) * self.altura
        return VolumenC
    def SuperCil(self):
        SuperficieC = (2*math.pi*self.radio*self.altura) + (2* math.pi * math.pow(self.radio,2))
        return SuperficieC

class Esfera(Figuras):
    def __init__(self,radio):
        self.radio = radio
    def VolEsf(self):
        VolumenE = (4/3)*math.pi*math.pow(self.radio,3)
        return VolumenE
    def SuperEsf(self):
        SuperficieE = 4*math.pi*math.pow(self.radio,2)
        return SuperficieE

class Piramide(Figuras):
    def __init__(self,base,altura,apotema):
        self.base = base
        self.altura = altura
        self.apotema = apotema
    def VolPir(self):
        VolumenP = (1/3)*(self.base)*(self.altura)*(self.apotema)
        return VolumenP
    def SuperPir(self):
        SuperP = math.pow(self.base,2) + (2*self.base*self.apotema)
        return SuperP
   

def Interfaz_Cilindro():
        radio = float(RadioCil.get())
        altura = float(AlturaCil.get())
        Cil = Cilindro(radio,altura)
        volumen = Cil.VolCil()
        superficie = Cil.SuperCil()
        if radio > 0 and altura > 0:
            messagebox.showinfo("Información del Cilindro", f"Volumen: {volumen}\nSuperficie: {superficie}")
        else:
            messagebox.showerror("Error", "Por favor, ingresa valores positivos.")


def Interfaz_Esfera():
        radio = float(RadioE.get())
        Esf = Esfera(radio)
        volumen = Esf.VolEsf()
        superficie = Esf.SuperEsf()
        if radio > 0:
            messagebox.showinfo("Información de la Esfera", f"Volumen: {volumen}\nSuperficie: {superficie}")
        else:
            messagebox.showerror("Error", "Por favor, ingresa valores positivos.")


def Interfaz_Piramide():
        base = float(BasePir.get())
        altura = float(AlturaPir.get())
        apotema = float(ApotemaPir.get())
        Pir = Piramide(base,altura,apotema)
        volumen = Pir.VolPir()
        superficie = Pir.SuperPir()
        if base > 0 and altura > 0 and apotema >0:
            messagebox.showinfo("Información de la Pirámide", f"Volumen: {volumen}\nSuperficie: {superficie}")
        else:
            messagebox.showerror("Error", "Por favor, ingresa valores positivos.")



def VentanaOpciones(seleccion):
    for widget in miFrame.winfo_children():
        widget.pack_forget()

    figura = FS.get()

    if figura == "Cilindro":
        Label(miFrame, text="Radio:", fg="Black", font=("Comic Sans MS",14)).pack(pady=10)
        RadioCil.pack()
        Label(miFrame, text="Altura:", fg="Black", font=("Comic Sans MS",14)).pack(pady=10)
        AlturaCil.pack()
        Button(miFrame, text="Calcular Datos", command=Interfaz_Cilindro).pack(pady=20)

    elif figura == "Esfera":
        Label(miFrame, text="Radio:", fg="Black", font=("Comic Sans MS",14)).pack(pady=10)
        RadioE.pack()
        Button(miFrame, text="Calcular Datos", command=Interfaz_Esfera).pack(pady=20)

    elif figura == "Piramide":
        Label(miFrame, text="Base:", fg="Black", font=("Comic Sans MS",14)).pack(pady=10)
        BasePir.pack()
        Label(miFrame, text="Altura:", fg="Black", font=("Comic Sans MS",14)).pack(pady=10)
        AlturaPir.pack()
        Label(miFrame, text="Radio:", fg="Black", font=("Comic Sans MS",14)).pack(pady=10)
        ApotemaPir.pack()
        Button(miFrame, text="Calcular Datos", command=Interfaz_Piramide).pack(pady=20)



raiz = Tk()
raiz.title("Datos Figuras Geométricas")
raiz.config(bg="Purple")


FS = StringVar()
FS.set("Selecciona una figura")

PreguntaLabel = Label(raiz, text="¿Qué figura desea analizar?:", fg="Black", font=("Comic Sans MS",14)).pack(pady=10)
MenuF = OptionMenu(raiz, FS, "Cilindro", "Esfera", "Piramide", command=VentanaOpciones)
MenuF.pack(pady=10)


miFrame = Frame(raiz)
miFrame.config(bg="Purple", cursor="pirate")
miFrame.pack(pady=10)


RadioCil = Entry(miFrame)
RadioCil.config(fg="Black", justify="center")
AlturaCil = Entry(miFrame)
AlturaCil.config(fg="Black", justify="center")
RadioE = Entry(miFrame)
RadioE.config(fg="Black", justify="center")
BasePir = Entry(miFrame)
BasePir.config(fg="Black", justify="center")
AlturaPir = Entry(miFrame)
AlturaPir.config(fg="Black", justify="center")
ApotemaPir = Entry(miFrame)
ApotemaPir.config(fg="black", justify="center")


raiz.mainloop()