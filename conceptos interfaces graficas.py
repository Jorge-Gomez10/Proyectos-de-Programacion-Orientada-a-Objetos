import tkinter as tk

class AplicacionGUI:
    def __init__(self, master):
        self.master = master
        master.title("Aplicación de Lista")

        self.etiqueta = tk.Label(master, text="Ingrese información:")
        self.etiqueta.pack()

        self.entrada = tk.Entry(master)
        self.entrada.pack()

        self.agregar_boton = tk.Button(master, text="Agregar", command=self.agregar_info)
        self.agregar_boton.pack()

        self.lista = tk.Listbox(master)
        self.lista.pack()

        self.limpiar_boton = tk.Button(master, text="Limpiar", command=self.limpiar_lista)
        self.limpiar_boton.pack()

    def agregar_info(self):
        info = self.entrada.get()
        if info:
            self.lista.insert(tk.END, info)
            self.entrada.delete(0, tk.END)

    def limpiar_lista(self):
        self.lista.delete(0, tk.END)

root = tk.Tk()
app = AplicacionGUI(root)
root.mainloop()

