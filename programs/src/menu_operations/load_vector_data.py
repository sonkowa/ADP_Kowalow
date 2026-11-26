import geopandas as gpd
from tkinter import filedialog, messagebox

from src.data_service import Layer, set_layer


def load_data_and_remember_outcome() -> bool:
    path = filedialog.askopenfilename(
        title="Wybierz warstwę",
        filetypes=[
            ("Obsługiwane formaty plików", "*.gpkg *.shp *.geojson *.json"),
            ("Wszystkie pliki", "*.*"),
        ],
    )
    if not path:
        return False

    try:
        data = gpd.read_file(path)
    except Exception as error:
        messagebox.showwarning(
            "Błąd wczytywania",
            "Nie udało się wczytać wybranego pliku.\n"
            "Upewnij się, że jest to prawidłowy plik wektorowy."
        )
        return False
    
    set_layer(Layer(kind="vector", data=data, path=path))
    return True