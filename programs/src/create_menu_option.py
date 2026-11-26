import tkinter as tk
from tkinter import messagebox
from collections.abc import Callable
from src.data_service import get_layer
from PIL import Image, ImageTk



def create_menu_option(
    canvas: tk.Canvas,
    height: int,
    text: str,
    *operations: Callable
):
    option_tag = f"menu_option_{height}"

    text_id = canvas.create_text(
        180,
        height,
        text=text,
        font=("Arial", 12, "normal"),
        fill="white",
        tags = (option_tag,)
    )

    left, top, right, bottom = canvas.bbox(text_id)
    padding_x = 12
    padding_y = 7
    width = right - left + padding_x * 2
    box_height = bottom - top + padding_y * 2

    overlay = Image.new("RGBA", (width, box_height), (0, 0, 0, 128))
    overlay_image = ImageTk.PhotoImage(overlay)

    if not hasattr(canvas, "_menu_background_images"):
        canvas._menu_background_images = []
    canvas._menu_background_images.append(overlay_image)

    background_id = canvas.create_image(
        (left + right) / 2,
        (top + bottom) / 2,
        image=overlay_image,
        tags=(option_tag,),
    )

    canvas.tag_lower(background_id, text_id)

    def on_click(event):
        for operation in operations:
            operation()

    def on_enter(event):
        canvas.itemconfig(text_id, fill="#00AEEF")

    def on_leave(event):
        canvas.itemconfig(text_id, fill="white")

    for item_id in (text_id, background_id):
        canvas.tag_bind(item_id, "<Button-1>", on_click)
        canvas.tag_bind(item_id, "<Enter>", on_enter)
        canvas.tag_bind(item_id, "<Leave>", on_leave)
