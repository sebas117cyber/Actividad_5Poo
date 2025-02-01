# punto 1 actividad 5

from tkinter import *
import math


class estudiante:
    def __init__(self, nota_1: float, nota_2: float, nota_3: float, nota_4: float, nota_5: float):
        self.nota_1 = nota_1
        self.nota_2 = nota_2
        self.nota_3 = nota_3
        self.nota_4 = nota_4
        self.nota_5 = nota_5
        self.lista_notes = [self.nota_1, self.nota_2, self.nota_3, self.nota_4, self.nota_5]

    def promedio(self):
        return sum(self.lista_notes) / len(self.lista_notes)
    
    def desviacion(self):
        prome = sum(self.lista_notes) / len(self.lista_notes)
        varianza = sum((i - prome) ** 2 for i in self.lista_notes) / (len(self.lista_notes) - 1)
        return math.sqrt(varianza)
    
    def mayor(self):
        maximo = max(self.lista_notes)
        return maximo

    def minimo(self):
        minimo = min(self.lista_notes)
        return minimo


def obtencion():
    N1 = float(nota1entry.get())
    N2 = float(nota2entry.get())
    N3 = float(nota3entry.get())
    N4 = float(nota4entry.get())
    N5 = float(nota5entry.get())

    return estudiante(N1, N2, N3, N4, N5)

def mpromedio():
    academico = obtencion()

    resullabel.config(text=f"Promedio: {round(academico.promedio(), 2)}")

def mdesviacion():
    academico = obtencion()

    resullabel.config(text=f"Desviacion estandar: {round(academico.desviacion(), 2)}")

def m_maximo():
    academico = obtencion()

    resullabel.config(text=f"Nota maxima: {academico.mayor()}")

def m_minimo():
    academico = obtencion()

    resullabel.config(text=f"Nota minima: {academico.minimo()}")

def mtodos():
    academico = obtencion()

    resullabel.config(text=(f"Promedio: {round(academico.promedio(), 2)}\n"
                            f"Desviacion estatndar: {round(academico.desviacion(), 2)}\n"
                            f"Nota maxima: {academico.mayor()}\n"
                            f"Nota minima: {academico.minimo()}"))
    



notas = Tk()
notas.title("Solución parte uno actividad 5")
notas.geometry("500x400")
notas.resizable(0, 0)
notas.config(bg="sky blue")

nota1etique = Label(notas, text="Ingrese la primer nota:", bd= 3, fg= "gray5", bg="sky blue")
nota1etique.place(x=50, y= 30)
nota1entry = Entry(notas)
nota1entry.place(x=185, y=30)

nota2etique = Label(notas, text="Ingrese la segunda nota:", bd= 3, fg= "gray5", bg="sky blue")
nota2etique.place(x=50, y= 60)
nota2entry = Entry(notas)
nota2entry.place(x=185, y=60)

nota3etique = Label(notas, text="Ingrese la tercera nota:", bd= 3, fg= "gray5", bg="sky blue")
nota3etique.place(x=50, y= 90)
nota3entry = Entry(notas)
nota3entry.place(x=185, y=90)

nota4etique = Label(notas, text="Ingrese la cuarta nota:", bd= 3, fg= "gray5", bg="sky blue")
nota4etique.place(x=50, y= 120)
nota4entry = Entry(notas)
nota4entry.place(x=185, y=120)

nota5etique = Label(notas, text="Ingrese la quinta nota:", bd= 3, fg= "gray5", bg="sky blue")
nota5etique.place(x=50, y= 150)
nota5entry = Entry(notas)
nota5entry.place(x=185, y=150)

caletique = Label(notas, text="Que desea calcular:", bd= 3, fg= "gray5", bg="sky blue")
caletique.place(x=175, y=170)

botonprome = Button(notas, width=15, text="promedio", bd= 4, fg= "gray5", bg="light goldenrod", command=mpromedio)
botonprome.place(x=20, y=190)

botondesvia = Button(notas, width=15, text="desviacion estandar", bd= 4, fg= "gray5", bg="light goldenrod", command=mdesviacion)
botondesvia.place(x=20, y=230)

botonmax = Button(notas, width=15, text="nota maxima", bd= 4, fg= "gray5", bg="light goldenrod", command=m_maximo)
botonmax.place(x=20, y=270)

botonmin = Button(notas, width=15, text="nota minima", bd= 4, fg= "gray5", bg="light goldenrod", command=m_minimo)
botonmin.place(x=20, y=310)

todoboton = Button(notas, width=15, text="todas las anteriores", bd= 4, fg= "gray5", bg="light goldenrod", command=mtodos)
todoboton.place(x=20, y=350)

resullabel = Label(notas, text= "", bg="light goldenrod", fg="black", bd=2)
resullabel.place(x=210, y=250)


notas.mainloop()