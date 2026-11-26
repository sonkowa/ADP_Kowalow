import rasterio as rio
from tkinter import filedialog, messagebox

from src.data_service import Layer, set_layer

    

def load_data_and_remember_outcome():
    path = filedialog.askopenfilename(
        title="Wybierz warstwę rastrową",
        filetypes=[
            ("GeoTIFF / TIFF", "*.tif *.tiff"),
            ("Wszystkie pliki", "*.*"),
        ],
    )

    if not path:
        return None

    try:
        with rio.open(path) as dataset:
            profile = dataset.profile.copy()


    except Exception as error:
        messagebox.showwarning(
            "Błąd wczytywania",
            "Nie udało się wczytać wybranego pliku.\n"
            "Upewnij się, że jest to prawidłowy plik rastrowy."
        )
        return False


    set_layer(Layer(kind="raster", data=path, path=path, profile=profile))
    return True