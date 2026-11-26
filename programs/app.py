from src.create_window import create_window
from src.create_menu_option import create_menu_option
from src.update_menu import update_menu
from src.create_layer_menu import create_layer_menu
from src.menu_operations.close_program import close_program
from src.menu_operations.load_vector_data import load_data_and_remember_outcome as vector_load
from src.menu_operations.load_raster_data import load_data_and_remember_outcome as raster_load

from src.menu_operations.show_layer import show_layer
from src.menu_operations.show_layer_info import show_layer_info



window, canvas = create_window()

def load_layer_and_open_menu(loader):
    if loader():
        update_menu(canvas)
        create_layer_menu(window)

create_menu_option(canvas, 400, "Wczytaj warstwę wektorową", lambda: load_layer_and_open_menu(vector_load), lambda: update_menu(canvas))
create_menu_option(canvas, 435, "Wczytaj warstwę rastrową", lambda: load_layer_and_open_menu(raster_load), lambda: update_menu(canvas))
create_menu_option(canvas, 470, "Zamknij program", lambda: close_program(window))

window.mainloop()