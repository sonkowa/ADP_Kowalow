from tkinter import messagebox
import rasterio as rio

from src.data_service import get_layer

def show_layer_info():
    layer = get_layer()

    if layer is None:
        return

    if layer.kind == "vector" :
        data = layer.data
        info = (
            f"Typ warstwy: wektorowa\n"
            f"Liczba obiektów: {len(data)}\n"
            f"Liczba kolumn: {len(data.columns)}\n"
            f"Typ geometrii: {', '.join(data.geom_type.unique())}\n"
            f"Układ współrzędnych: {data.crs}"
    )

    elif layer.kind == "raster":
        with rio.open(layer.data) as data:
            info = (
                f"Typ warstwy: rastrowa\n"
                f"Wymiary (szer. × wys.): "
                f"{data.width} × {data.height}\n"
                f"Liczba pasm: {data.count}\n"
                f"Typ danych: {', '.join(dict.fromkeys(data.dtypes))}\n"
                f"Układ współrzędnych: {data.crs}\n"
                f"Rozdzielczość: {data.res}\n"
                f"Zasięg: {data.bounds}",
                f"Metadane: {data.tags()}"
            )
    else:
        messagebox.showwarning(
            "Nieznany typ warstwy",
            f"Nieobsługiwany typ: {layer.kind}",
        )
        return
    messagebox.showinfo(
        "Informacje o warstwie",
        info
    )
