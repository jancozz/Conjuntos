from tkinter import messagebox

class Controller:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.view.on_create_set = self.create_set
        self.view.on_perform_operation = self.perform_operation

    def create_set(self, set_name, elements):
        self.model.create_set(set_name, elements)
        messagebox.showinfo("Conjunto Creado", f"Conjunto {set_name} creado exitosamente: {elements}")

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
            elif operation == "Es subconjunto":
                result = self.model.is_subset(set_name, second_set_name)
            elif operation == "Es superconjunto":
                result = self.model.is_superset(set_name, second_set_name)
            self.view.update_result(result)
        except KeyError:
            messagebox.showerror("Operation Error", "Uno o ambos conjuntos no se encontraron.")