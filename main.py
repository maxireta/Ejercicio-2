from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedStyle

class Aplicacion():
    __ventana = None
    __precioIVA = None
    __precioSinIVA = None
    __iva = None

    def __init__(self):
      
        self.__ventana = Tk()
        self.__ventana.geometry('300x300')
        self.__ventana.configure(bg='lightgrey')
        self.__ventana.title('Cálculo del IVA')
        
        self.__style = ThemedStyle(self.__ventana)
        self.__style.set_theme('clam') 

        self.__style.configure("Calcular.TButton", background="lightgreen", borderwidth=5,bordercolor='green' , borderradius=5, padding=1)
        self.__style.configure("Salir.TButton", background="pink", bordercolor='red', borderwidth=5, borderradius=5, padding=1)

        mainframe = ttk.Frame(self.__ventana, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe['borderwidth'] = 2
        mainframe['relief'] = 'sunken'
        self.__precioIVA = StringVar()
        self.__precioSinIVA = StringVar()
        self.__iva = StringVar()
        

        ttk.Label(mainframe, text=" Precio sin IVA").grid(column=1, row=1, sticky=W)
        precioSinIVAEntry = ttk.Entry(mainframe, width=10, textvariable=self.__precioSinIVA)
        precioSinIVAEntry.grid(column=3, row=1, sticky=(W, E))

        ttk.Radiobutton(mainframe, text='IVA 21 %', value=21, variable=self.__iva,
        command=self.cambiaValorIVA).grid(row =2, column=1, columnspan=1, sticky='w')
        ttk.Radiobutton(mainframe, text='IVA 10.5 %', value=10.5, variable=self.__iva, 
        command=self.cambiaValorIVA).grid(row =3, column=1, columnspan=2,sticky='w')

        ttk.Label(mainframe, text="IVA ").grid(column=1, row=4, sticky=W)
        ivaEntry = ttk.Entry(mainframe, width=10, textvariable=self.__iva)
        ivaEntry.grid(column=3, row=4, sticky=(W, E))

        ttk.Label(mainframe, text=" Precio Con IVA ").grid(column=1, row=5, sticky=W)
        precioIVAEntry = ttk.Entry(mainframe, width=10, textvariable=self.__precioIVA)
        precioIVAEntry.grid(column=3, row=5, sticky=(W, E))

        ttk.Button(mainframe, text="Calcular ", command=self.calcular, style="Calcular.TButton").grid(column=1, row=6, sticky=W)
        ttk.Button(mainframe, text='Salir', command=self.__ventana.destroy, style='Salir.TButton').grid(column=3, row=6, sticky=W)


        for child in mainframe.winfo_children():
            child.grid_configure(padx=10, pady=7)
        
        self.__ventana.mainloop()
    

    def cambiaValorIVA(self):
        iva_value = float(self.__iva.get())
        self.__iva.set(iva_value)


    def calcular(self):
        try:
            precioSinIVA = float(self.__precioSinIVA.get())
            iva = float(self.__iva.get())

            if iva == 21:
               porcentajeIVA = float(self.__precioSinIVA.get())* 21/100
            else:
                porcentajeIVA = float(self.__precioSinIVA.get()) *10.5 /100

            precioIVA = precioSinIVA + porcentajeIVA

            self.__precioIVA.set(str(precioIVA))
            self.__precioIVAEntry.insert(0, self.__precioIVA.get())
       
        except ValueError:
            messagebox.showerror(title='Error', message='Ingrese un valor numérico')
        

def testAPP():
    mi_app = Aplicacion()

if __name__ == '__main__':
    testAPP()
