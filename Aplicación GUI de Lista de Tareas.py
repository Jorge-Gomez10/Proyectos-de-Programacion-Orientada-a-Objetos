
import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        self.tasks = []

        # Crear los componentes de la interfaz gráfica
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.task_list = tk.Listbox(root, width=50)
        self.task_list.pack(padx=10, pady=10)

        # Manejar eventos de teclado
        self.task_entry.bind("<Return>", self.add_task_event)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.update_task_list()

            # Limpiar el campo de entrada
            self.task_entry.delete(0, tk.END)

    def complete_task(self):
        selection = self.task_list.curselection()
        if selection:
            index = selection[0]
            task = self.tasks[index]
            self.tasks[index] = f"✓ {task}" if not task.startswith("✓") else task.lstrip("✓ ")
            self.update_task_list()

    def delete_task(self):
        selection = self.task_list.curselection()
        if selection:
            index = selection[0]
            del self.tasks[index]
            self.update_task_list()

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for task in self.tasks:
            self.task_list.insert(tk.END, task)

    def add_task_event(self, event):
        self.add_task()

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
