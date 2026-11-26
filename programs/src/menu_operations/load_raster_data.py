import rasterio as rio
from tkinter import filedialog, messagebox

from src.data_service import set_layer


def load_data_and_remember_outcome():
    layer = load_data()
    set_layer(layer)
    

def load_data():
    path = filedialog.askopenfilename(
        title="Wybierz warstwę rastrową"
    )

    if not path:
        return None

    try:
        layer = rio.read_file(path)
    except Exception:
        messagebox.showwarning(
            "Błąd wczytywania",
            "Nie udało się wczytać wybranego pliku.\n"
            "Upewnij się, że jest to prawidłowy plik rastrowy."
        )
        return None

    return layer