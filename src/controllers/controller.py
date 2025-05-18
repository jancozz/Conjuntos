from ast import literal_eval
from tkinter import messagebox
import random


class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.view.on_create_set = self.create_set
        self.view.on_perform_operation = self.perform_operation
        self.view.on_check_relation = self.check_relation
        self.view.on_generate_random_relation = self.generate_random_relation

    def create_set(self, set_name, elements):
        self.model.create_set(set_name, elements)
        # messagebox.showinfo("Conjunto Creado", f"Conjunto {set_name} creado exitosamente: {elements}")
        self.update_created_sets()

    def perform_operation(self, set_name, second_set_name, operation):
        try:
            if operation == "Union":
                result = self.model.union(set_name, second_set_name)
            elif operation == "Interseccion":
                result = self.model.intersection(set_name, second_set_name)
            elif operation == "Differencia":
                result = self.model.difference(set_name, second_set_name)
            elif operation == "Differencia simetrica":
                result = self.model.symmetric_difference(set_name, second_set_name)
            elif operation == "Es subconjunto de":
                result = self.model.is_subset(set_name, second_set_name)
            elif operation == "Es superconjunto de":
                result = self.model.is_superset(set_name, second_set_name)
            elif operation == "Son iguales":
                result = self.model.is_equal(set_name, second_set_name)
            elif operation == "Son disjuntos":
                result = self.model.is_disjoint(set_name, second_set_name)

            first_set_elements = self.model.get_set(set_name)
            second_set_elements = self.model.get_set(second_set_name)

            self.view.update_operation_set_labels(first_set_elements, second_set_elements)

            self.view.update_operation_result(result)
        except KeyError:
            messagebox.showerror("Operation Error", "Uno o ambos conjuntos no se encontraron.")

    def update_created_sets(self):
        all_sets = self.model.get_all_sets()
        sets_text = ""
        for set_name, elements in all_sets.items():
            sets_text += f"{set_name} = {sorted(elements)}\n"
        self.view.update_created_sets_display(sets_text)

    def check_relation(self, first_set_name, second_set_name, relation_set, relation_type):

        if not first_set_name or not second_set_name:
            messagebox.showerror("Input Error", "Ambos nombres de conjuntos son requeridos.")
            return

        if first_set_name not in self.model.sets or second_set_name not in self.model.sets:
            messagebox.showerror("Set Error", "Uno o ambos conjuntos no existen.")
            return

        try:
            relation_set = literal_eval(relation_set)  # Convierte el string a una lista de tuplas
            if not all(isinstance(pair, tuple) and len(pair) == 2 for pair in relation_set):
                raise ValueError("La relación debe ser una lista de tuplas de dos elementos.")

            if relation_type == "Reflexiva":
                result = self.model.is_reflexive(first_set_name, second_set_name, relation_set)
            elif relation_type == "Simetrica":
                result = self.model.is_symmetric(first_set_name, second_set_name, relation_set)
            elif relation_type == "Antisimetrica":
                result = self.model.is_antisymmetric(first_set_name, second_set_name, relation_set)
            elif relation_type == "Transitiva":
                result = self.model.is_transitive(first_set_name, second_set_name, relation_set)

            first_set_elements = self.model.get_set(first_set_name)
            second_set_elements = self.model.get_set(second_set_name)

            self.view.update_relation_set_labels(first_set_elements, second_set_elements)

            self.view.update_relation_result(result)

        except (SyntaxError, ValueError) as e:
            messagebox.showerror("Input Error", f"El formato de la relación no es válido: {e}")

    def generate_random_relation(self, first_set_name, second_set_name, relation_type):
        set1 = self.model.get_set(first_set_name)
        set2 = self.model.get_set(second_set_name)

        if not set1:
            raise ValueError(f"El conjunto {first_set_name} debe contener al menos un elemento.")
        if not set2:
            raise ValueError(f"El conjunto {second_set_name} debe contener al menos un elemento.")

        if relation_type == "Reflexiva":
            relation = self.model.generate_reflexive_set(first_set_name, second_set_name)
        elif relation_type == "Simetrica":
            relation = self.model.generate_random_symmetric_set(first_set_name, second_set_name)
        elif relation_type == "Antisimetrica":
            relation = self.model.generate_random_antisymmetric_set(first_set_name, second_set_name)
        elif relation_type == "Transitiva":
            relation = self.model.generate_random_transitive_set(first_set_name, second_set_name)

        first_set_elements = self.model.get_set(first_set_name)
        second_set_elements = self.model.get_set(second_set_name)

        self.view.update_relation_set_labels(first_set_elements, second_set_elements)

        self.view.update_random_set_entry(relation)
