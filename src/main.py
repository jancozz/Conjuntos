import tkinter as tk
from views.view import View
from controllers.controller import Controller
from models.model import SetOperationsModel as Model


def main():
    root = tk.Tk()
    root.title("App Conjuntos")
    root.geometry("450x350")

    model = Model()
    view = View(root)
    controller = Controller(view, model)

    root.mainloop()


if __name__ == "__main__":
    main()