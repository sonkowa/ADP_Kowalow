import rasterio as rio
from tkinter import filedialog, messagebox

from src.data_service import get_layer


def save_data():
    layer = get_layer()

    if layer is None:
        return

    if layer.kind == "raster":
        path = filedialog.asksaveasfilename(
            title="Zapisz raster",
            defaultextension=".tif",
            filetypes=[("GeoTIFF", "*.tif *.tiff")],
        )
        if not path:
            return
        try:
            with rio.open(layer.data) as source:
                profile = (
                    layer.profile.copy()
                    if layer.profile is not None
                    else source.profile.copy()
                )
                profile.update(driver="GTiff")

            with rio.open(path, "w", **profile) as destination:
                destination.write(source.read())
                destination.update_tags(**source.tags())

                for band_index in range(1, source.count + 1):
                    destination.update_tags(
                        band_index,
                        **source.tags(band_index),
                    )
    
        except Exception as error:
            messagebox.showwarning(
                "Błąd zapisu",
                f"Nie udało się zapisać rastra:\n{error}",
            )
            return

    elif layer.kind == "vector":
        path = filedialog.asksaveasfilename(
            title="Zapisz warstwę wektorową",
            defaultextension=".geojson",
            filetypes=[
                ("GeoJSON", "*.geojson"),
                ("GeoPackage", "*.gpkg"),
                ("Shapefile", "*.shp"),
                ("CSV", "*.csv"),
            ],
        )

        if not path:
            return
        try:
                if path.endswith(".csv"):
                    layer.to_csv(path, index=False)
                else:
                    layer.to_file(path)
        
                messagebox.showinfo(
                    "Zapisano plik",
                    "Warstwa została zapisana poprawnie."
                )

        except Exception:
            messagebox.showwarning(
                "Błąd zapisu",
                "Nie udało się zapisać warstwy."
            )
        messagebox.showinfo("Zapisano plik", "Warstwa została zapisana poprawnie.")