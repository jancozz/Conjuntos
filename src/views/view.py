import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from customtkinter import *


class View:
    def __init__(self, master):
        self.master = master
        self.master.configure(bg="blue")

        # Crear el contenedor de las pestañas
        self.notebook = ttk.Notebook(master)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Crear las vistas para las pestañas
        self.create_set_tab = CTkFrame(self.notebook, fg_color="#343434")
        self.operations_tab = CTkFrame(self.notebook, fg_color="#343434")
        self.relations_tab = CTkFrame(self.notebook, fg_color="#343434")

        # Añadir las pestañas al Notebook
        self.notebook.add(self.create_set_tab, text=" Crear Conjunto ")
        self.notebook.add(self.operations_tab, text="  Operaciones  ")
        self.notebook.add(self.relations_tab, text="   Relaciones   ")

        # ** VISTA "CREAR CONJUNTO" **

        self.set_name_label = CTkLabel(self.create_set_tab, text="Nombre:", text_color="#e8e8e8",
                                       font=("Arial", 13, "bold"))
        self.set_name_label.pack(pady=(30, 0))

        self.set_name_entry = CTkEntry(self.create_set_tab, width=90, font=("Arial", 13))
        self.set_name_entry.pack(pady=(0, 20))

        self.set_elements_label = CTkLabel(self.create_set_tab, text="Elementos (separados por comas):",
                                           font=("Arial", 13, "bold"))
        self.set_elements_label.pack()

        self.set_elements_entry = CTkEntry(self.create_set_tab, font=("Arial", 13))
        self.set_elements_entry.pack(pady=(0, 20))

        self.create_set_button = CTkButton(self.create_set_tab, text="Crear Conjunto", font=("Arial", 13),
                                           command=self.create_set,
                                           fg_color="#134F6C")
        self.create_set_button.pack()

        self.sets_frame = CTkFrame(self.create_set_tab, fg_color="#292929")
        self.sets_frame.pack(fill="both", expand=True, pady=20, padx=120)

        self.created_sets_label = CTkLabel(self.sets_frame, text="", font=("Arial", 13))
        self.created_sets_label.pack()

        self.created_sets_display = CTkLabel(self.sets_frame, text="", font=("Arial", 13))
        self.created_sets_display.pack()

        # ** VISTA "OPERACIONES" **

        self.top_frame = CTkFrame(self.operations_tab, fg_color="#343434")
        self.top_frame.pack(side="top", fill="both", padx=65, pady=(30, 0))

        self.frame1 = CTkFrame(self.top_frame, fg_color="#343434")
        self.frame1.pack(side="left", fill="both", expand=True, padx=(10, 0))

        self.frame2 = CTkFrame(self.top_frame, fg_color="#343434")
        self.frame2.pack(side="right", fill="both", expand=True, padx=(0, 10))

        # Cuadro de entrada para el primer conjunto
        self.first_set_name_label = CTkLabel(self.frame1, text="1er Conjunto:", font=("Arial", 13, "bold"))
        self.first_set_name_label.pack()

        self.first_set_name_entry = CTkEntry(self.frame1, width=90, font=("Arial", 13))
        self.first_set_name_entry.pack()

        self.first_set_values_label_op = CTkLabel(self.frame1, text="[ ]", font=("Arial", 13))
        self.first_set_values_label_op.pack()

        # Cuadro de entrada para el segundo conjunto
        self.second_set_name_label = CTkLabel(self.frame2, text="2do Conjunto:", font=("Arial", 13, "bold"))
        self.second_set_name_label.pack()

        self.second_set_name_entry = CTkEntry(self.frame2, width=90, font=("Arial", 13))
        self.second_set_name_entry.pack()

        self.second_set_values_label_op = CTkLabel(self.frame2, text="[ ]", font=("Arial", 13))
        self.second_set_values_label_op.pack()

        # Widgets para las operaciones entre conjuntos
        self.operation_label = CTkLabel(self.operations_tab, text="Operacion:", font=("Arial", 13, "bold"))
        self.operation_label.pack(pady=(20, 0))

        self.operation_var = StringVar(self.operations_tab)
        self.operation_var.set("Union")

        self.operations_menu = CTkOptionMenu(
            self.operations_tab,
            fg_color="#5b5b5b",
            button_color="#5b5b5b",
            button_hover_color="#464646",
            dropdown_fg_color="#464646",
            dropdown_hover_color="#5b5b5b",
            variable=self.operation_var,
            anchor="center",
            values=["Union", "Interseccion", "Differencia", "Differencia simetrica",
                    "Es subconjunto de", "Es superconjunto de", "Son iguales", "Son disjuntos"], font=("Arial", 13)
        )

        self.operations_menu.pack(pady=(0, 15))

        self.result_label = CTkLabel(self.operations_tab, text="Resultado:", font=("Arial", 13, "bold"))
        self.result_label.pack()

        self.result_display = CTkLabel(self.operations_tab, text="-", font=("Arial", 13))
        self.result_display.pack()

        self.operation_button = CTkButton(self.operations_tab, text="Realizar Operacion", font=("Arial", 13),
                                          command=self.perform_operation, fg_color="#134F6C")
        self.operation_button.pack(pady=(10, 0))

        # ** VISTA "RELACIONES" **

        self.top_frame_relations = CTkFrame(self.relations_tab, fg_color="#343434")
        self.top_frame_relations.pack(side="top", fill="both", padx=65, pady=(30, 0))

        self.frame1_relations = CTkFrame(self.top_frame_relations, fg_color="#343434")
        self.frame1_relations.pack(side="left", fill="both", expand=True, padx=(10, 0))

        self.frame2_relations = CTkFrame(self.top_frame_relations, fg_color="#343434")
        self.frame2_relations.pack(side="right", fill="both", expand=True, padx=(0, 10))

        # Cuadro de entrada para el primer conjunto
        self.first_set_name_label = CTkLabel(self.frame1_relations, text="1er Conjunto:", font=("Arial", 13, "bold"))
        self.first_set_name_label.pack()

        self.first_set_name_relations_entry = CTkEntry(self.frame1_relations, width=90, font=("Arial", 13))
        self.first_set_name_relations_entry.pack()

        self.first_set_values_label_re = CTkLabel(self.frame1_relations, text="[ ]", font=("Arial", 13))
        self.first_set_values_label_re.pack()

        # Cuadro de entrada para el segundo conjunto
        self.second_set_name_label = CTkLabel(self.frame2_relations, text="2do Conjunto:", font=("Arial", 13, "bold"))
        self.second_set_name_label.pack()

        self.second_set_name_relations_entry = CTkEntry(self.frame2_relations, width=90, font=("Arial", 13))
        self.second_set_name_relations_entry.pack()

        self.second_set_values_label_re = CTkLabel(self.frame2_relations, text="[ ]", font=("Arial", 13))
        self.second_set_values_label_re.pack()

        self.set_relation_label = CTkLabel(self.relations_tab, text="Definir una relacion (pares ordenados):",
                                           font=("Arial", 13, "bold"))
        self.set_relation_label.pack(pady=(20, 0))

        self.set_relation_entry = CTkEntry(self.relations_tab, width=180,
                                           placeholder_text="(1,'b'),('a','c'),(2,3),('c',2)", font=("Arial", 13))
        self.set_relation_entry.pack(pady=(0, 20))

        self.relation_label = CTkLabel(self.relations_tab, text="Relacion:", font=("Arial", 13, "bold"))
        self.relation_label.pack()

        self.relation_var = StringVar(self.relations_tab)
        self.relation_var.set("Reflexiva")

        self.relations_menu = CTkOptionMenu(
            self.relations_tab,
            fg_color="#5b5b5b",
            button_color="#5b5b5b",
            button_hover_color="#464646",
            dropdown_fg_color="#464646",
            dropdown_hover_color="#5b5b5b",
            variable=self.relation_var,
            anchor="center",
            values=["Reflexiva", "Simetrica", "Antisimetrica", "Transitiva"], font=("Arial", 13)
        )
        self.relations_menu.pack(pady=(0, 15))

        self.result_main_frame = CTkFrame(self.relations_tab, fg_color="#343434")
        self.result_main_frame.pack(fill="both", padx=155)

        self.result_label_frame = CTkFrame(self.result_main_frame, fg_color="#343434")
        self.result_label_frame.pack(side="left", fill="both", expand=False, padx=(10, 0))

        self.result_display_frame = CTkFrame(self.result_main_frame, fg_color="#343434")
        self.result_display_frame.pack(side="right", fill="both", expand=True, padx=(0, 10))

        self.result_label = CTkLabel(self.result_label_frame, text="Resultado:", font=("Arial", 13, "bold"))
        self.result_label.pack(side="right")

        self.result_relation_display = CTkLabel(self.result_display_frame, text="-", font=("Arial", 13))
        self.result_relation_display.pack(pady=5)

        self.validate_relation_button = CTkButton(self.relations_tab, text="Comprobar Relacion",
                                                  font=("Arial", 13),
                                                  command=self.check_relation,
                                                  fg_color="#134F6C")
        self.validate_relation_button.pack(pady=(15, 0))

    # Metodos
    def create_set(self):
        set_name = self.set_name_entry.get()
        elements = self.set_elements_entry.get()
        if set_name and elements:
            elements = [el.strip() for el in elements.split(",")]
            self.on_create_set(set_name, elements)
        else:
            messagebox.showerror("Input Error", "El nombre y los elementos del conjunto son requeridos.")

    def on_create_set(self, set_name, elements):
        """Este método será invocado por el controlador cuando se cree un conjunto"""
        pass

    def perform_operation(self):
        first_set_name = self.first_set_name_entry.get()
        second_set_name = self.second_set_name_entry.get()
        operation = self.operation_var.get()

        if first_set_name and second_set_name:
            self.on_perform_operation(first_set_name, second_set_name, operation)
        else:
            messagebox.showerror("Input Error", "Los nombres de ambos conjuntos son requeridos.")

    def on_perform_operation(self, first_set_name, second_set_name, operation):
        """Este método será invocado por el controlador cuando se realice una operación"""
        pass

    def update_operation_result(self, result):
        self.result_display.configure(text=str(result))

    def update_operation_set_labels(self, first_set_elements, second_set_elements):
        first_set_text = f"[{', '.join(map(str, sorted(first_set_elements)))}]"
        second_set_text = f"[{', '.join(map(str, sorted(second_set_elements)))}]"
        self.first_set_values_label_op.configure(text=first_set_text)
        self.second_set_values_label_op.configure(text=second_set_text)

    def update_created_sets_display(self, sets_text):
        self.created_sets_label.configure(text="Conjuntos:")
        self.created_sets_display.configure(text=sets_text)

    def update_relation_set_labels(self, first_set_elements, second_set_elements):
        first_set_text = f"[{', '.join(map(str, sorted(first_set_elements)))}]"
        second_set_text = f"[{', '.join(map(str, sorted(second_set_elements)))}]"
        self.first_set_values_label_re.configure(text=first_set_text)
        self.second_set_values_label_re.configure(text=second_set_text)

    def check_relation(self):
        first_set_name = self.first_set_name_relations_entry.get()
        second_set_name = self.second_set_name_relations_entry.get()
        relation_set = self.set_relation_entry.get()
        relation_type = self.relation_var.get()
        if first_set_name and second_set_name:
            self.on_check_relation(first_set_name, second_set_name, relation_set, relation_type)
        else:
            messagebox.showerror("Input Error",
                                 "Los nombres de ambos conjuntos y la relacion de pares ordenados son requeridos")

    def update_relation_result(self, result):
        self.result_relation_display.configure(text=str(result))

    def on_check_relation(self, first_set_name, second_set_name, relation_set, relation_type):
        pass
