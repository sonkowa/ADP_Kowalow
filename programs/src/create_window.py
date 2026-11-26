import tkinter as tk


def create_window():
    # Utworzenie głównego okna + canvas:

    window = tk.Tk()
    window.title("GeoTools")
    window.resizable(False, False)

    canvas = tk.Canvas(
        window,
        width=650,
        height=650,
        highlightthickness=0
    )

    canvas.pack()


    # Grafika tła:

    window.background_screen = tk.PhotoImage(
        file="src/img/minozaur.png"
    )

    canvas.create_image(
        0,
        -100,
        image=window.background_screen,
        anchor="nw"
    )


    # Tytuł programu:
    canvas.create_text(
        200,
        50,
        text="GeoTools",
        font=("Arial", 30, "bold"),
        fill="white"
    )


    # Menu:

    canvas.create_text(
        180,
        280,
        text="Wybierz operację:",
        font=("Arial", 12, "normal"),
        fill="black"
    )

    return (window, canvas)