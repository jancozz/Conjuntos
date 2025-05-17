from customtkinter import *
from views.view import View
from controllers.controller import Controller
from models.model import SetOperationsModel as Model


def main():
    root = CTk()
    root.title("App Conjuntos")
    root.geometry("450x450")

    model = Model()
    view = View(root)
    controller = Controller(view, model)

    root.mainloop()


if __name__ == "__main__":
    main()
