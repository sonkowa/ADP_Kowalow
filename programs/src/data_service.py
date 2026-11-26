
from dataclasses import dataclass
from typing import Literal

import geopandas as gpd


@dataclass
class Layer:
    kind: Literal["vector", "raster"]
    data: object
    path: str
    profile: dict | None = None


_layer: Layer | None = None


def set_layer(layer: Layer) -> None:
    global _layer
    _layer = layer


def get_layer() -> Layer | None:
    return _layer