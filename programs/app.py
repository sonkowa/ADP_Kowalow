from src.create_window import create_window
from src.create_menu_option import create_menu_option
from src.update_menu import update_menu
from src.menu_operations.close_program import close_program
from src.menu_operations.load_vector_data import load_data_and_remember_outcome as vector_load
from src.menu_operations.load_raster_data import load_data_and_remember_outcome as raster_load
from src.menu_operations.show_layer import show_layer
from src.menu_operations.show_layer_info import show_layer_info
from src.menu_operations.save_data import save_data


window, canvas = create_window()


create_menu_option(canvas, 320, "Wczytaj warstwę wektorową", lambda: vector_load(), lambda: update_menu(canvas))
create_menu_option(canvas, 350, "Wczytaj warstwę rastrową", lambda: raster_load(), lambda: update_menu(canvas))
create_menu_option(canvas, 380, "Wyświetl warstwę", lambda: show_layer())
create_menu_option(canvas, 410, "Wyświetl informacje o warstwie", lambda: show_layer_info())
create_menu_option(canvas, 440, "Zapisz warstwę", lambda: save_data())
create_menu_option(canvas, 470, "Zamknij program", lambda: close_program(window))

window.mainloop()