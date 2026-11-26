import rasterio as rio
from tkinter import filedialog, messagebox

from src.data_service import get_layer



def save_raster(layer):
    output_path = filedialog.asksaveasfilename(
        title="Zapisz warstwę rastrową",
        defaultextension=".tif",
        filetypes=[("GeoTIFF", "*.tif *.tiff")],
    )

    if not output_path:
        return
    try:
        with rio.open(layer.path) as source:
            pixels = source.read()
            profile = (
                layer.profile.copy()
                if layer.profile is not None
                else source.profile.copy()
            )
            tags = source.tags()
            band_tags = [
                source.tags(index)
                for index in range(1, source.count + 1)
            ]

            profile.update(
                driver="GTiff",
                width=source.width,
                height=source.height,
                count=source.count,
                crs=source.crs,
                transform=source.transform,
            )

        with rio.open(output_path, "w", **profile) as destination:
            destination.write(pixels)
            destination.update_tags(**tags)

            for index, tags_for_band in enumerate(band_tags, start=1):
                if tags_for_band:
                    destination.update_tags(index, **tags_for_band)

    except Exception as error:
        messagebox.showwarning(
            "Błąd zapisu",
            f"Nie udało się zapisać warstwy:\n{error}",
        )
        return

    messagebox.showinfo(
        "Zapisano plik",
        "Warstwa została zapisana poprawnie",
    )




def save_data():
    layer = get_layer()

    if layer is None:
        return

    if layer.kind == "raster":
        save_raster(layer)
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