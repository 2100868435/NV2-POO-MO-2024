import tkinter as tk
from tkinter import messagebox

class Tarea:
    def __init__(self, texto):  # Corregido a __init__
        self.texto = texto
        self.completada = False

class Aplicacion:
    def __init__(self, root):  # Corregido a __init__
        self.root = root
        self.root.title("Gestión de Tareas")
        self.tareas = []  # Lista para almacenar las tareas
        self.crear_widgets()

    def crear_widgets(self):
        self.entrada_tarea = tk.Entry(self.root, width=40)  # Campo de entrada
        self.entrada_tarea.grid(row=0, column=0, padx=5, pady=5)

        self.boton_anadir = tk.Button(self.root, text="Añadir", command=self.anadir_tarea)
        self.boton_anadir.grid(row=0, column=1, padx=5, pady=5)

        self.lista_tareas = tk.Listbox(self.root, width=40)  # Lista de tareas
        self.lista_tareas.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.boton_completar = tk.Button(self.root, text="Completar", command=self.completar_tarea)
        self.boton_completar.grid(row=2, column=0, padx=5, pady=5)

        self.boton_eliminar = tk.Button(self.root, text="Eliminar", command=self.eliminar_tarea)
        self.boton_eliminar.grid(row=2, column=1, padx=5, pady=5)

        # Atajos de teclado
        self.root.bind("<Return>", self.anadir_tarea_con_enter)
        self.root.bind("c", self.completar_tarea_con_tecla)
        self.root.bind("d", self.eliminar_tarea_con_tecla)
        self.root.bind("<Escape>", self.cerrar_aplicacion)

    def anadir_tarea(self):
        texto = self.entrada_tarea.get()  # Obtener texto de entrada
        if texto:  # Asegurarse de que no esté vacío
            tarea = Tarea(texto)  # Crear una nueva tarea
            self.tareas.append(tarea)  # Añadir la tarea a la lista
            self.lista_tareas.insert(tk.END, texto)  # Mostrar la tarea en la lista
            self.entrada_tarea.delete(0, tk.END)  # Limpiar el campo de entrada

    def anadir_tarea_con_enter(self, evento):
        self.anadir_tarea()  # Llama a la función al presionar Enter

    def completar_tarea(self):
        indice = self.lista_tareas.curselection()  # Obtener la tarea seleccionada
        if indice:  # Si hay una tarea seleccionada
            tarea = self.tareas[indice[0]]  # Obtener la tarea de la lista
            tarea.completada = True  # Marcar la tarea como completada
            self.lista_tareas.itemconfig(indice, fg="green")  # Cambiar color a verde

    def completar_tarea_con_tecla(self, evento):
        self.completar_tarea()  # Completar la tarea al presionar 'c'

    def eliminar_tarea(self):
        indice = self.lista_tareas.curselection()  # Obtener la tarea seleccionada
        if indice:  # Si hay una tarea seleccionada
            self.tareas.pop(indice[0])  # Eliminar la tarea de la lista
            self.lista_tareas.delete(indice)  # Eliminar la tarea de la interfaz

    def eliminar_tarea_con_tecla(self, evento):
        self.eliminar_tarea()  # Eliminar la tarea al presionar 'd'

    def cerrar_aplicacion(self, evento):
        self.root.destroy()  # Cerrar la aplicación

if __name__ == "__main__":  # Corregido a __name__ y __main__
    root = tk.Tk()
    aplicacion = Aplicacion(root)
    root.mainloop()  # Iniciar el bucle principal de la interfaz

