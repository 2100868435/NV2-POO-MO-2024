import tkinter as tk
from tkinter import messagebox

class ListaDeTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Lista de Tareas")
        self.root.geometry("400x300")

        # Lista para almacenar las tareas
        self.tareas = []

        # Campo de entrada para las tareas
        self.entry_tarea = tk.Entry(root, width=30)
        self.entry_tarea.pack(pady=10)
        self.entry_tarea.bind("<Return>", self.agregar_tarea_evento)

        # Botones de control
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        self.btn_agregar = tk.Button(frame_botones, text="Añadir Tarea", command=self.agregar_tarea)
        self.btn_agregar.pack(side=tk.LEFT, padx=5)

        self.btn_completar = tk.Button(frame_botones, text="Marcar como Completada", command=self.marcar_completada)
        self.btn_completar.pack(side=tk.LEFT, padx=5)

        self.btn_eliminar = tk.Button(frame_botones, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.btn_eliminar.pack(side=tk.LEFT, padx=5)

        # Listbox para mostrar las tareas
        self.listbox_tareas = tk.Listbox(root, selectmode=tk.SINGLE, width=45, height=10)
        self.listbox_tareas.pack(pady=10)
        self.listbox_tareas.bind("<Double-1>", self.marcar_completada_evento)

    def agregar_tarea(self):
        tarea = self.entry_tarea.get().strip()
        if tarea:
            self.tareas.append(tarea)
            self.actualizar_lista()
            self.entry_tarea.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "No se puede agregar una tarea vacía.")

    def agregar_tarea_evento(self, event):
        self.agregar_tarea()

    def marcar_completada(self):
        seleccion = self.listbox_tareas.curselection()
        if seleccion:
            index = seleccion[0]
            self.tareas[index] += " ✔"
            self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para marcarla como completada.")

    def marcar_completada_evento(self, event):
        self.marcar_completada()

    def eliminar_tarea(self):
        seleccion = self.listbox_tareas.curselection()
        if seleccion:
            index = seleccion[0]
            self.tareas.pop(index)
            self.actualizar_lista()
        else:
            messagebox.showwarning("Advertencia", "Seleccione una tarea para eliminarla.")

    def actualizar_lista(self):
        self.listbox_tareas.delete(0, tk.END)
        for tarea in self.tareas:
            self.listbox_tareas.insert(tk.END, tarea)

if __name__ == "__main__":
    root = tk.Tk()
    app = ListaDeTareasApp(root)
    root.mainloop()
