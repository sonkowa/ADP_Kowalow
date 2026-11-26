import tkinter as tk

from src.menu_operations.save_data import save_data
from src.menu_operations.show_layer_info import show_layer_info
from src.menu_operations.show_layer import show_layer


def create_layer_menu(parent: tk.Tk) -> None:
    dialog = tk.Toplevel(parent)
    dialog.title("Funkcje warstwy")
    dialog.resizable(False, False)
    dialog.transient(parent)

    tk.Label(
        dialog,
        text="Wybierz funkcję dla wczytanej warstwy:",
        padx=20,
        pady=12,
    ).pack()

    tk.Button(
        dialog,
        text="Podgląd informacji",
        command=show_layer_info,
    ).pack(fill="x", padx=20, pady=4)

    tk.Button(
        dialog,
        text="Podgląd warstwy",
        command=show_layer,
    ).pack(fill="x", padx=20, pady=4)

    tk.Button(
        dialog,
        text="Zapisz",
        command=save_data,
    ).pack(fill="x", padx=20, pady=4)

    tk.Button(
        dialog,
        text="Wyjście",
        command=dialog.destroy,
    ).pack(fill="x", padx=20, pady=(4, 16))

    dialog.grab_set()
    parent.wait_window(dialog)