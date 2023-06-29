from tkinter import *
from tkinter import ttk
from tkinter import font

class ventana:
    def __init__(self):
        self.__ventana = Tk()
        self.__ventana.geometry("300x300")
        self.__ventana.title("Calculo de IVA")
        self.__base = StringVar()
        self.__piva = StringVar()
        self.__iva = StringVar()
        self.__valor = IntVar()
        self.__c = PhotoImage(file="boton_calcular.png")
        self.__s = PhotoImage(file="boton_salir.png")
        tamaño = font.Font(size=15)
        ttk.Label(self.__ventana, text= "Precio sin IVA", font= ("neosans", 9)).place(x=30, y=30)
        precio = ttk.Entry(self.__ventana, width=10, font=tamaño, textvariable= self.__base).place(x=150, y=27)
        ttk.Radiobutton(self.__ventana, text= "   IVA 21 %", value= 1, variable= self.__valor).place(x=30, y=80)
        ttk.Radiobutton(self.__ventana, text= "   IVA 10.5 %", value= 0, variable= self.__valor).place(x=30, y=110)
        ttk.Label(self.__ventana, text= "IVA", font= ("neosans", 9)).place(x=60, y=150)
        ttk.Label(self.__ventana, textvariable= self.__iva, width=10, font=tamaño, background="white", borderwidth= 2, relief="solid").place(x=150, y=150)
        ttk.Label(self.__ventana, text="Precio con IVA", font= ("neosans", 9)).place(x=30, y=180)
        ttk.Label(self.__ventana, textvariable= self.__piva, width=10, font=tamaño, background="white", borderwidth= 2, relief="solid").place(x=150, y=180)
        cal = Button(self.__ventana, image= self.__c, borderwidth=0, command= self.calcular).place(x=30, y=245)
        sal = Button(self.__ventana, image= self.__s, borderwidth=0, command= self.__ventana.destroy).place(x=190, y=245)
        self.__ventana.mainloop()
    def calcular(self):
        if self.__valor.get() == 0:
            base = float(self.__base.get())
            piva = base * 10.5/100
            self.__piva.set(piva)
            self.__iva.set(10.5)
        elif self.__valor.get() == 1:
            base = float(self.__base.get())
            piva = base * 21/100
            self.__piva.set(piva)
            self.__iva.set(21)
        #Precio Base*10.5/100 para los artículos grabados con el 10.5%
        #Precio Base * 21/100 para los artículos grabados con el 21%