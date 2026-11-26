import matplotlib.pyplot as plt
import rasterio as rio 

from src.data_service import get_layer

def show_layer():
    layer = get_layer()

    if layer is None:
        return

    fig, ax = plt.subplots()

    if layer.kind == "vector":
        layer.plot()
        plt.show()
    elif layer.kind == "raster":
        with rio.open(layer.data) as dataset:
            if dataset.count >= 3: # dla rastrów trzypasmowych 
                pixels = dataset.read([1,2,3])
                rgb = pixels.transpose(1,2,0)
                ax.imshow(rgb)
            elif dataset.count == 1:
                # raster 1 pasmo
                pixels = dataset.read(1)
                ax.imshow(pixels, cmap = "gray")
        ax.set_title("Podgląd rastra")

    ax.axis("off")
    fig.tight_layout()
    plt.show()


