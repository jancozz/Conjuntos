import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class View:
    def __init__(self, master):
        self.master = master

        # Crear el contenedor de las pestañas
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Crear las vistas para las pestañas
        self.create_set_tab = ttk.Frame(self.notebook)
        self.operations_tab = ttk.Frame(self.notebook)

        # Añadir las pestañas al Notebook
        self.notebook.add(self.create_set_tab, text="Crear Conjunto")
        self.notebook.add(self.operations_tab, text="Operaciones")

        # ** VISTA "Crear Conjunto" **

        # Widgets para la creación de conjuntos
        self.set_name_label = tk.Label(self.create_set_tab, text="Nombre:")
        self.set_name_label.pack(pady=(40, 0))

        self.set_name_entry = tk.Entry(self.create_set_tab, width=10)
        self.set_name_entry.pack(pady=(0, 20))

        self.set_elements_label = tk.Label(self.create_set_tab, text="Elementos (separados por comas):")
        self.set_elements_label.pack()

        self.set_elements_entry = tk.Entry(self.create_set_tab)
        self.set_elements_entry.pack(pady=(0, 20))

        self.create_set_button = tk.Button(self.create_set_tab, text="Crear Conjunto", command=self.create_set)
        self.create_set_button.pack()

        # ** VISTA "Operaciones" **

        # Cuadro de entrada para el primer conjunto
        self.first_set_name_label = tk.Label(self.operations_tab, text="Primer Conjunto:")
        self.first_set_name_label.pack(pady=(20, 0))

        self.first_set_name_entry = tk.Entry(self.operations_tab, width=10)
        self.first_set_name_entry.pack(pady=(0, 20))

        # Widgets para las operaciones entre conjuntos
        self.operation_label = tk.Label(self.operations_tab, text="Operacion:")
        self.operation_label.pack()

        self.operation_var = tk.StringVar(self.operations_tab)
        self.operation_var.set("Union")

        self.operations_menu = tk.OptionMenu(self.operations_tab, self.operation_var, "Union", "Interseccion",
                                             "Differencia", "Differencia simetrica", "Es subconjunto",
                                             "Es superconjunto")
        self.operations_menu.pack(pady=(0, 20))

        # Cuadro de entrada para el segundo conjunto
        self.second_set_name_label = tk.Label(self.operations_tab, text="Segundo Conjunto:")
        self.second_set_name_label.pack()

        self.second_set_name_entry = tk.Entry(self.operations_tab, width=10)
        self.second_set_name_entry.pack(pady=(0, 20))

        self.result_label = tk.Label(self.operations_tab, text="Resultado:")
        self.result_label.pack()

        self.result_display = tk.Label(self.operations_tab, text="")
        self.result_display.pack()

        self.operation_button = tk.Button(self.operations_tab, text="Realizar Operacion",
                                          command=self.perform_operation)
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
        self.result_display.config(text=str(result))

    def on_create_set(self, set_name, elements):
        """Este método será invocado por el controlador cuando se cree un conjunto"""
        pass

    def on_perform_operation(self, first_set_name, second_set_name, operation):
        """Este método será invocado por el controlador cuando se realice una operación"""
        pass
