import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from customtkinter import *


class View:
    def __init__(self, master):
        self.master = master

        # Crear el contenedor de las pestañas
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Crear las vistas para las pestañas
        self.create_set_tab = CTkFrame(self.notebook, fg_color="#343434")
        self.operations_tab = CTkFrame(self.notebook, fg_color="#343434")

        # Añadir las pestañas al Notebook
        self.notebook.add(self.create_set_tab, text="Crear Conjunto")
        self.notebook.add(self.operations_tab, text="Operaciones")

        # ** VISTA "Crear Conjunto" **

        # Widgets para la creación de conjuntos
        self.set_name_label = CTkLabel(self.create_set_tab, text="Nombre:", text_color="#e8e8e8")
        self.set_name_label.pack(pady=(40, 0))

        self.set_name_entry = CTkEntry(self.create_set_tab, width=70)
        self.set_name_entry.pack(pady=(0, 20))

        self.set_elements_label = CTkLabel(self.create_set_tab, text="Elementos (separados por comas):")
        self.set_elements_label.pack()

        self.set_elements_entry = CTkEntry(self.create_set_tab)
        self.set_elements_entry.pack(pady=(0, 20))

        self.create_set_button = CTkButton(self.create_set_tab, text="Crear Conjunto", command=self.create_set,
                                           fg_color="#134F6C")
        self.create_set_button.pack()

        # ** VISTA "Operaciones" **

        self.top_frame = CTkFrame(self.operations_tab, fg_color="#343434")
        self.top_frame.pack(side="top", fill="both", padx=45, pady=(40, 20))

        frame1 = CTkFrame(self.top_frame, fg_color="#343434")
        frame1.pack(side="left", fill="both", expand=True, padx=40)

        frame2 = CTkFrame(self.top_frame, fg_color="#343434")
        frame2.pack(side="right", fill="both", expand=True, padx=40)

        # Cuadro de entrada para el primer conjunto
        self.first_set_name_label = CTkLabel(frame1, text="1er Conjunto:")
        self.first_set_name_label.pack()

        self.first_set_name_entry = CTkEntry(frame1, width=70)
        self.first_set_name_entry.pack()

        # Cuadro de entrada para el segundo conjunto
        self.second_set_name_label = CTkLabel(frame2, text="2do Conjunto:")
        self.second_set_name_label.pack()

        self.second_set_name_entry = CTkEntry(frame2, width=70)
        self.second_set_name_entry.pack()

        # Widgets para las operaciones entre conjuntos
        self.operation_label = CTkLabel(self.operations_tab, text="Operacion:")
        self.operation_label.pack()

        self.operation_var = StringVar(self.operations_tab)
        self.operation_var.set("Union")

        self.operations_menu = CTkOptionMenu(
            self.operations_tab,
            fg_color="#5b5b5b",
            button_color="#5b5b5b",
            button_hover_color="#464646",
            dropdown_fg_color="#464646",
            variable=self.operation_var,
            anchor="center",
            values=["Union", "Interseccion", "Differencia", "Differencia simetrica",
                    "Es subconjunto de", "Es superconjunto de", "Igualdad", "Disjuncion"]
        )

        self.operations_menu.pack(pady=(0, 20))

        self.result_label = CTkLabel(self.operations_tab, text="Resultado:")
        self.result_label.pack()

        self.result_display = CTkLabel(self.operations_tab, text="")
        self.result_display.pack()

        self.operation_button = CTkButton(self.operations_tab, text="Realizar Operacion",
                                          command=self.perform_operation, fg_color="#134F6C")
        self.operation_button.pack(pady=(20, 0))

    # Metodos
    def create_set(self):
        set_name = self.set_name_entry.get()
        elements = self.set_elements_entry.get()
        if set_name and elements:
            elements = [el.strip() for el in elements.split(",")]
            self.on_create_set(set_name, elements)
        else:
            messagebox.showerror("Input Error", "El nombre y los elementos del conjunto son requeridos.")

    def perform_operation(self):
        first_set_name = self.first_set_name_entry.get()
        second_set_name = self.second_set_name_entry.get()
        operation = self.operation_var.get()

        if first_set_name and second_set_name:
            self.on_perform_operation(first_set_name, second_set_name, operation)
        else:
            messagebox.showerror("Input Error", "Los nombres de ambos conjuntos son requeridos.")

    def update_result(self, result):
        self.result_display.configure(text=str(result))

    def on_create_set(self, set_name, elements):
        """Este método será invocado por el controlador cuando se cree un conjunto"""
        pass

    def on_perform_operation(self, first_set_name, second_set_name, operation):
        """Este método será invocado por el controlador cuando se realice una operación"""
        pass
