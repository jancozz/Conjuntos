from customtkinter import *
from views.view import View
from controllers.controller import Controller
from models.model import SetOperationsModel as Model


def main():
    root = CTk()
    root.title("App Conjuntos")
    root.geometry(
        f"{450}x{450}+{int(root.winfo_screenwidth() / 2 - 225)}+{int(root.winfo_screenheight() / 2 - 225)}")

    model = Model()
    view = View(root)
    Controller(view, model)

    root.mainloop()


if __name__ == "__main__":
    main()
